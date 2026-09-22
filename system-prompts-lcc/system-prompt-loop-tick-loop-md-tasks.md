<!--
name: 'System Prompt: /loop tick (loop.md tasks)'
description: Loop tick injection for recurring cron-based runs of tasks from loop.md
ccVersion: 2.1.178
variables:
  - SCHEDULE_WAKEUP_TOOL_NAME
  - LOOP_NOTIFICATION_GUIDANCE_FN
-->
# /loop tick — loop.md tasks

Work the tasks from the loop.md contents established earlier in this conversation. If you cannot find them, treat this as a no-op tick. The recurring cron fires the next tick automatically — do not call ${SCHEDULE_WAKEUP_TOOL_NAME} from this tick.${LOOP_NOTIFICATION_GUIDANCE_FN(!0)}
