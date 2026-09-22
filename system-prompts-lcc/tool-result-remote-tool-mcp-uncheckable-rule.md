<!--
name: 'Remote Tool: MCP Rule This Session Cannot Check'
description: >-
  Refusal when a forwarded MCP call has a field-level rule this session cannot
  evaluate, so every forwarded call is refused.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_TOOL_MCP_UNCHECKABLE_RULE_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_MCP_UNCHECKABLE_RULE_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_MCP_UNCHECKABLE_RULE_VAR_2
  - TOOL_RESULT_REMOTE_TOOL_MCP_UNCHECKABLE_RULE_VAR_3
-->
${TOOL_RESULT_REMOTE_TOOL_MCP_UNCHECKABLE_RULE_VAR_0(TOOL_RESULT_REMOTE_TOOL_MCP_UNCHECKABLE_RULE_VAR_1.name,TOOL_RESULT_REMOTE_TOOL_MCP_UNCHECKABLE_RULE_VAR_2)} Rules on this tool apply to a forwarded call field by field; one this session cannot check that way (a field the tool does not declare, or a structured value) refuses every forwarded call, and a plain rule on mcp__${TOOL_RESULT_REMOTE_TOOL_MCP_UNCHECKABLE_RULE_VAR_3} covers every attached machine's tools.
