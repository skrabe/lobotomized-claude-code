<!--
name: 'REPL: MCP Undeclared Arguments'
description: >-
  Refusal when a REPL MCP call passes arguments the server does not declare;
  lists accepted names and points to describeTool.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_MCP_UNDECLARED_ARGS_VAR_0
  - TOOL_RESULT_REPL_MCP_UNDECLARED_ARGS_VAR_1
  - TOOL_RESULT_REPL_MCP_UNDECLARED_ARGS_VAR_2
  - TOOL_RESULT_REPL_MCP_UNDECLARED_ARGS_VAR_3
-->
Not sent: ${TOOL_RESULT_REPL_MCP_UNDECLARED_ARGS_VAR_0} does not declare ${TOOL_RESULT_REPL_MCP_UNDECLARED_ARGS_VAR_1}. A server can drop an argument it does not declare and answer with that parameter's default instead. It takes: ${TOOL_RESULT_REPL_MCP_UNDECLARED_ARGS_VAR_2(TOOL_RESULT_REPL_MCP_UNDECLARED_ARGS_VAR_3).join(", ")}. Call it again with those names; describeTool('${TOOL_RESULT_REPL_MCP_UNDECLARED_ARGS_VAR_0}') describes each one.
