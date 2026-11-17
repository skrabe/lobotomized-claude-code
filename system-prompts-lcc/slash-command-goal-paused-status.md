<!--
name: 'Slash command: goal paused status'
description: '/goal status output when the goal is paused, with Claude''s pause reason.'
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_GOAL_PAUSED_STATUS_VAR_0
  - SLASH_COMMAND_GOAL_PAUSED_STATUS_VAR_1
  - SLASH_COMMAND_GOAL_PAUSED_STATUS_VAR_2
-->
Goal paused: ${SLASH_COMMAND_GOAL_PAUSED_STATUS_VAR_0.condition} (${SLASH_COMMAND_GOAL_PAUSED_STATUS_VAR_1})${SLASH_COMMAND_GOAL_PAUSED_STATUS_VAR_2}
Send a message to continue, or run /goal clear.
Claude's reason: ${SLASH_COMMAND_GOAL_PAUSED_STATUS_VAR_0.paused.reason}
