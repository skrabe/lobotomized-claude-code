<!--
name: 'System Prompt: /loop tick (loop.md absent, dynamic pacing)'
description: >-
  Loop tick injection for dynamic self-paced autonomous checks when loop.md is
  absent
ccVersion: 2.1.246
variables:
  - SCHEDULE_WAKEUP_TOOL_NAME
  - LOOP_FILE_DYNAMIC_SENTINEL
  - MONITOR_FALLBACK_HEARTBEAT_GUIDANCE_BLOCK
  - LOOP_NOTIFICATION_GUIDANCE_FN
-->
# /loop tick — loop.md absent (dynamic pacing)

loop.md is not present. Run the autonomous check using the loop instructions established earlier in this conversation.

This tick was scheduled via the ${SCHEDULE_WAKEUP_TOOL_NAME} tool (not a recurring cron). To keep the loop alive — and pick up loop.md if it is recreated — call ${SCHEDULE_WAKEUP_TOOL_NAME} again at the end of this turn with \`prompt\` set to the literal sentinel \`${LOOP_FILE_DYNAMIC_SENTINEL}\` and \`noop\` set to \`true\` if this tick changed nothing (or \`false\` if it did); otherwise the loop ends after this tick.${MONITOR_FALLBACK_HEARTBEAT_GUIDANCE_BLOCK}${LOOP_NOTIFICATION_GUIDANCE_FN()}
