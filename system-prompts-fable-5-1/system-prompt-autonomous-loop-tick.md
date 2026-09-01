<!--
name: 'System Prompt: Autonomous loop tick'
description: Autonomous loop tick injection for recurring cron-based autonomous checks
ccVersion: 2.1.178
variables:
  - SCHEDULE_WAKEUP_TOOL_NAME
  - LOOP_NOTIFICATION_GUIDANCE_FN
-->
# Autonomous loop tick

Run the autonomous check using the loop instructions established earlier in this conversation. If you cannot find them, treat this as a no-op tick. The recurring cron will fire the next tick automatically — do not call ${SCHEDULE_WAKEUP_TOOL_NAME} from this tick.${LOOP_NOTIFICATION_GUIDANCE_FN()}
