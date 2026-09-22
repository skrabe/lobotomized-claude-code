<!--
name: 'Tool result: Claude Design result truncated'
description: >-
  Model-facing tool_result text block appended by kBm when ClaudeDesign result
  blocks exceed the aggregate char cap and are omitted.
ccVersion: 2.1.199
variables:
  - TOOL_RESULT_CLAUDE_DESIGN_TRUNCATED_VAR_0
  - TOOL_RESULT_CLAUDE_DESIGN_TRUNCATED_VAR_1
  - TOOL_RESULT_CLAUDE_DESIGN_TRUNCATED_VAR_2
  - TOOL_RESULT_CLAUDE_DESIGN_TRUNCATED_VAR_3
-->
[ClaudeDesign result truncated — ${TOOL_RESULT_CLAUDE_DESIGN_TRUNCATED_VAR_0} block(s) (${TOOL_RESULT_CLAUDE_DESIGN_TRUNCATED_VAR_1.round(TOOL_RESULT_CLAUDE_DESIGN_TRUNCATED_VAR_2/1024)}k chars) omitted; aggregate over ${TOOL_RESULT_CLAUDE_DESIGN_TRUNCATED_VAR_1.round(TOOL_RESULT_CLAUDE_DESIGN_TRUNCATED_VAR_3/1024)}k-char cap]
