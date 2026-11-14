<!--
name: 'Tool Result: Subagent handback auto mode blocked warning'
description: >-
  Warns that auto mode blocked a subagent's report, giving the reason, and asks
  for careful review before acting
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_SUBAGENT_HANDBACK_AUTO_MODE_BLOCKED_WARNING_VAR_0
  - TOOL_RESULT_SUBAGENT_HANDBACK_AUTO_MODE_BLOCKED_WARNING_VAR_1
  - TOOL_RESULT_SUBAGENT_HANDBACK_AUTO_MODE_BLOCKED_WARNING_VAR_2
-->
${TOOL_RESULT_SUBAGENT_HANDBACK_AUTO_MODE_BLOCKED_WARNING_VAR_0}: auto mode blocked this subagent's report. Reason: ${TOOL_RESULT_SUBAGENT_HANDBACK_AUTO_MODE_BLOCKED_WARNING_VAR_1(TOOL_RESULT_SUBAGENT_HANDBACK_AUTO_MODE_BLOCKED_WARNING_VAR_2)}. The report follows; review the subagent's actions carefully before acting on it.
