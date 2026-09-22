<!--
name: 'Skill: /stuck slash command'
description: Diagnozse frozen or slow Claude Code sessions
ccVersion: 2.1.141
-->
# /stuck — diagnose frozen/slow Claude Code sessions

The user thinks another Claude Code session on this machine is frozen, stuck, or very slow. Investigate and report.

## What to look for

Scan for other Claude Code processes, excluding the current one (exclude the PID running this prompt). Process names are typically `claude` (installed) or `cli` (native dev build).

Signs of a stuck session:
- **High CPU (≥90%) sustained** — likely an infinite loop. Sample twice, 1-2s apart, to rule out a transient spike.
- **State `D` (uninterruptible sleep)** — often an I/O hang. First char of the `state` column in `ps`; ignore modifiers (`+`, `s`, `<`).
- **State `T` (stopped)** — probably a stray Ctrl+Z.
- **State `Z` (zombie)** — parent isn't reaping.
- **Very high RSS (≥4GB)** — possible memory leak.
- **Stuck child process** — a hung `git`, `node`, or shell subprocess can freeze the parent. Check `pgrep -lP <pid>`.

## Investigation steps

1. List Claude Code processes (macOS/Linux):
   ```
   ps -axo pid=,pcpu=,rss=,etime=,state=,comm=,command= | grep -E '(claude|cli)' | grep -v grep
   ```
   Keep rows where `comm` is `claude`, or `cli` with "claude" in the command path.

2. For anything suspicious, gather context:
   - Child processes: `pgrep -lP <pid>`
   - High CPU: sample again after 1-2s to confirm it's sustained
   - Hung child (e.g. a git command): note its full command line via `ps -p <child_pid> -o command=`
   - If you can infer the session ID, check `~/.claude/debug/<session-id>.txt` — the last few hundred lines often show what it was doing before hanging

3. For a truly frozen process, optionally `sample <pid> 3` (macOS) for a 3-second native stack sample. It's large — grab it only when the process is clearly hung and you want to know why.

## Report

Post to Slack only if you actually found something stuck. If every session looks healthy, tell the user that directly — do not post an all-clear to the channel.

If you found a stuck/slow session, post to **#claude-code-feedback** (channel ID: `C07VBSHV7EV`) via the Slack MCP tool (ToolSearch for `slack_send_message` if it isn't loaded). Use a two-message structure:

1. **Top-level message** — one line: hostname, Claude Code version, terse symptom (e.g. "PID 12345 pegged at 100% CPU for 10min"). No code blocks.
2. **Thread reply** (pass the top message's `ts` as `thread_ts`) — the full dump: PID, CPU%, RSS, state, uptime, command line, child processes; your diagnosis; any debug-log tail or `sample` output.

If Slack MCP isn't available, format the report as a copy-pasteable message and tell the user to thread the details.

## Notes
- Diagnostic only — don't kill or signal any processes.
- If the user named a specific PID or symptom, focus there first.
