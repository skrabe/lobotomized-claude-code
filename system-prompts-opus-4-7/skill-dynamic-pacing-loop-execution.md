<!--
name: 'Skill: Dynamic pacing loop execution'
description: >-
  Step-by-step instructions for executing a dynamic pacing loop that runs tasks,
  arms persistent monitors for event-gated waits, schedules fallback heartbeat
  ticks, and handles task notifications
ccVersion: 2.1.246
variables:
  - TASK_RUN_LABEL
  - MONITOR_TOOL_NAME
  - SCHEDULE_WAKEUP_TOOL_NAME
  - TASK_LIST_TOOL_NAME
  - CONFIRMATION_MESSAGE
  - DYNAMIC_MODE_SENTINEL
  - TASK_STOP_TOOL_NAME
  - ADDITIONAL_INFO_FN
-->
1. **Run TASK_RUN_LABEL now**, following the instructions inlined below.
2. **If the next tick is gated on an event** (CI finishing, a PR comment, a log line) and no MONITOR_TOOL_NAME is already running for it: arm one now with `persistent: true`. Its events wake this loop immediately — you do not wait for the SCHEDULE_WAKEUP_TOOL_NAME deadline. Arm once; on later ticks call TASK_LIST_TOOL_NAME first and skip if a monitor is already running.
3. **Briefly confirm**: DYNAMIC_MODE_SENTINEL, whether a TASK_STOP_TOOL_NAME is the primary wake signal, and what fallback delay you're about to pick. Write this as text *before* calling ADDITIONAL_INFO_FN — the turn ends as soon as that tool returns.
4. **Then, as the last action of this turn, call CONFIRMATION_MESSAGE** with:
   - `delaySeconds`: with a P2 armed this is the fallback heartbeat (lean 1200–1800s). Without one, pick based on what you observed this turn — quiet branch? wait longer. Lots in flight? wait shorter. Read the tool's own description for cache-aware delay guidance.
   - `reason`: one short sentence on why you picked that delay.
   - `prompt`: the literal string `G` — the dynamic-mode sentinel expands at fire time to the full instructions (first fire / first fire post-compact / loop.md edited) or a dynamic-pacing-specific short reminder (subsequent fires). Do not pass the full instructions; that is handled automatically.
   - `noop`: `true` if this tick changed nothing ("still waiting", "quiet hold"); `false` if it did something worth keeping. Consecutive `noop: true` ticks collapse in the terminal.
5. **If woken by a `<task-notification>`** rather than this prompt: handle the event, then call U again with `G` and the same 1200–1800s `delaySeconds` — the P2 remains the wake signal; this only resets the safety net.
6. **To stop the loop**, omit the U call and YU any P2 you armed (use WR to find the task ID if it is no longer in context).MLK
