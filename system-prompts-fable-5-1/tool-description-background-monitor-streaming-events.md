<!--
name: 'Tool Description: Background monitor (streaming events)'
description: >-
  Describes the background monitor tool that streams stdout events from
  long-running scripts as chat notifications, with guidelines on script quality,
  output volume, and selective filtering
ccVersion: 2.1.210
variables:
  - BACKGROUND_TASKS_DISABLED
-->

Start a background monitor that streams stdout events from a long-running script. Each stdout line is an event that arrives as a chat notification while you keep working; events arrive on their own schedule and are not user replies, even if one lands while you await an answer. Exit ends the watch.

Pick by how many notifications you need:
- **One** (server ready, build finishes) → Bash with `run_in_background` when background tasks are available, or foreground Bash when they are not and a command that exits when true, e.g. \`until grep -q "Ready in" dev.log; do sleep 0.5; done\`.
- **One per occurrence, indefinitely** (every ERROR line) → Monitor with an unbounded command (\`tail -f\`, \`inotifywait -m\`, \`while true\`).
- **One per occurrence, until a known end** (each CI step, stop when the run completes) → Monitor with a command that emits lines then exits.

  # Each matching log line is an event
  tail -f /var/log/app.log | grep --line-buffered "ERROR"

  # Each file change is an event
  inotifywait -m --format '%e %f' /watched/dir

  # Poll GitHub for new PR comments, one line per new comment
  last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  while true; do
    now=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    gh api "repos/owner/repo/issues/123/comments?since=$last" --jq '.[] | "\\(.user.login): \\(.body)"'
    last=$now; sleep 30
  done

  # Per-occurrence with a natural end: emit each CI check as it lands, exit when the run completes
  prev=""
  while true; do
    s=$(gh pr checks 123 --json name,bucket)
    cur=$(jq -r '.[] | select(.bucket!="pending") | "\\(.name): \\(.bucket)"' <<<"$s" | sort)
    comm -13 <(echo "$prev") <(echo "$cur")
    prev=$cur
    jq -e 'all(.bucket!="pending")' <<<"$s" >/dev/null && break
    sleep 30
  done

Don't use an unbounded command for a single notification. \`tail -f\`, \`inotifywait -m\`, and \`while true\` never exit on their own, so the monitor stays armed until timeout even after the event fires — use Bash with `run_in_background` when background tasks are available, or foreground Bash when they are not and an \`until\` loop instead. \`tail -f log | grep -m 1 ...\` does not fix this: if the log goes quiet after the match, \`tail\` never receives SIGPIPE and the pipeline hangs.

Script quality:
- Every pipe stage must flush per line, or matches sit in its buffer for minutes: \`grep\` needs \`--line-buffered\`, \`awk\` needs \`fflush()\`. \`head\` can't flush — \`| head -N\` emits nothing until N matches accumulate, then ends the stream.
- In poll loops, handle transient failures (\`curl ... || true\`) so one failed request doesn't kill the monitor.
- Poll intervals: 30s+ for remote APIs (rate limits), 0.5-1s for local checks.
- Write a specific \`description\` — it appears in every notification ("errors in deploy.log", not "watching logs").
- Only stdout triggers notifications. Stderr goes to the output file (readable via Read) but is silent — for a command you run directly, merge it with \`2>&1\` so failures reach your filter (no effect when tailing an existing log).

Coverage: a filter must match every terminal state, not just the happy path. A monitor that greps only for the success marker stays silent through a crashloop, hang, or unexpected exit — and silence looks identical to "still running." For poll loops, emit on every terminal status (\`succeeded|failed|cancelled|timeout\`); if you can't enumerate the failure signatures, broaden the alternation rather than narrow it.

  # Silent on crash, hang, or any non-success exit
  tail -f run.log | grep --line-buffered "elapsed_steps="

  # Covers progress plus the failure signatures you'd act on
  tail -f run.log | grep -E --line-buffered "elapsed_steps=|Traceback|Error|FAILED|assert|Killed|OOM"

Output volume: every stdout line is a conversation message, so filter for the lines you'd act on — both success and failure signals, never raw logs. Monitors producing too many events are stopped automatically; restart with a tighter filter. Stdout lines within 200ms batch into one notification, so multiline output from a single event groups naturally.

The script runs in the same shell environment as Bash. Exit ends the watch (exit code reported); timeout kills it. Set \`persistent: true\` for session-length watches (PR monitoring, log tails) — it runs until you call TaskStop or the session ends. Use TaskStop to cancel early.
