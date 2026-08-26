<!--
name: 'Skill: /loop self-pacing mode'
description: >-
  Instructs Claude how to self-pace a recurring loop by arming event monitors as
  primary wake signals and scheduling fallback heartbeat delays between
  iterations
ccVersion: 2.1.246
variables:
  - MONITOR_TOOL_NAME
  - SCHEDULE_WAKEUP_TOOL_NAME
  - TASK_LIST_TOOL_NAME
  - TASK_STOP_TOOL_NAME
  - ADDITIONAL_INFO_FN
-->
The user wants you to self-pace. Decide what makes the next iteration worth running — a passage of time, or an observable event.

1. **Run the parsed prompt now.** If it's a slash command, invoke it via the Skill tool; otherwise act on it directly.
2. **If the next run is gated on an event** (CI finishing, a log line matching, a file changing, a PR comment) and no ${MONITOR_TOOL_NAME} is already running for it: arm one now with \`persistent: true\`. Its events arrive as \`<task-notification>\` messages and wake this loop immediately — you don't wait for the ${SCHEDULE_WAKEUP_TOOL_NAME} deadline. Arm once; on later iterations call ${TASK_LIST_TOOL_NAME} first and skip this step if a monitor is already running.
3. **Briefly confirm** as text: that you're self-pacing, whether a ${MONITOR_TOOL_NAME} is the primary wake signal, that you ran the task now, and the fallback delay you're about to pick. Write this *before* calling ${SCHEDULE_WAKEUP_TOOL_NAME} — the turn ends as soon as that tool returns.
4. **As the last action of this turn, decide whether the loop continues.** If it needs another iteration, call ${SCHEDULE_WAKEUP_TOOL_NAME} with:
   - \`delaySeconds\`: with a ${MONITOR_TOOL_NAME} armed this is the fallback heartbeat — how long to wait if no event fires (lean 1200–1800s; idle ticks more frequent than the task needs are pure overhead). Without a ${MONITOR_TOOL_NAME} this is the cadence — pick based on what you observed. See the tool's own description for cache-aware delay guidance.
   - \`reason\`: one short sentence on why you picked that delay.
   - \`prompt\`: the full original /loop input verbatim, prefixed with \`/loop \` so the next firing re-enters this skill and continues the loop (e.g. if the user typed \`/loop check the deploy\`, pass \`/loop check the deploy\`).
   - \`noop\`: \`true\` if this tick changed nothing ("still waiting", "quiet hold"); \`false\` if it did something worth keeping. Consecutive \`noop: true\` ticks collapse in the terminal.
   If it doesn't, stop instead (step 6) — re-arming is a per-turn choice, not a default.
5. **If woken by a \`<task-notification>\`** rather than this prompt: handle the event in the context of the loop task, then make the same continue-or-stop decision. To continue, call ${SCHEDULE_WAKEUP_TOOL_NAME} again with the same \`prompt\` and the same 1200–1800s \`delaySeconds\` from step 4 — the ${MONITOR_TOOL_NAME} remains the wake signal; this only resets the safety net. If the event means the work is done, stop (step 6).
6. **To stop the loop** — task complete, no further progress possible, or the user asked — call ${SCHEDULE_WAKEUP_TOOL_NAME} with \`stop: true\` (no other fields) and ${TASK_STOP_TOOL_NAME} any ${MONITOR_TOOL_NAME} you armed (use ${TASK_LIST_TOOL_NAME} to find the task ID if it's no longer in context).${ADDITIONAL_INFO_FN()}
