<!--
name: No Teammate On Team (Lead-Only Spawn)
description: >-
  SendMessage tool-error returned to the model when no teammate by that name is
  on the team and this agent cannot spawn one itself, so it must ask the lead to
  spawn one.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_SEND_MESSAGE_NO_TEAMMATE_LEAD_ONLY_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_NO_TEAMMATE_LEAD_ONLY_VAR_1
-->
No teammate named '${TOOL_RESULT_SEND_MESSAGE_NO_TEAMMATE_LEAD_ONLY_VAR_0}' is currently on team '${TOOL_RESULT_SEND_MESSAGE_NO_TEAMMATE_LEAD_ONLY_VAR_1}'. Message the lead to spawn one.
