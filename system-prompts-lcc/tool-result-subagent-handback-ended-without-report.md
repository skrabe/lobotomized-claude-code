<!--
name: Subagent Handback Ended Without Report
description: >-
  Agent-tool harness note that the subagent ended without delivering a report
  through SendMessage.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_SUBAGENT_HANDBACK_ENDED_WITHOUT_REPORT_VAR_0
  - TOOL_RESULT_SUBAGENT_HANDBACK_ENDED_WITHOUT_REPORT_VAR_1
-->
The subagent ended without delivering a report through ${TOOL_RESULT_SUBAGENT_HANDBACK_ENDED_WITHOUT_REPORT_VAR_0}, so no report was delivered. Its unsent text is not shown.${TOOL_RESULT_SUBAGENT_HANDBACK_ENDED_WITHOUT_REPORT_VAR_1?" Send the agent a message (SendMessage) to ask it to deliver its report.":""}
