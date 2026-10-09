<!--
name: Output objects require launch rules
description: Requests an ordinary call when launch permission settings are absent.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_TOOL_OUTPUT_NO_LAUNCH_RULES_VAR_0
-->
${TOOL_RESULT_SERVED_TOOL_OUTPUT_NO_LAUNCH_RULES_VAR_0} was not run: this server holds no permission rules (CLAUDE_CODE_MCP_SERVE_SETTINGS was unset or empty when it started), and it returns output objects only for calls it can judge. Call it without asking for its output object.
