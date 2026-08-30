<!--
name: Coordinator MCP prompt not invocable
description: >-
  Meta message injected into the coordinator conversation when it tries to run
  an MCP prompt that cannot run in coordinator mode.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_COORDINATOR_MCP_PROMPT_NOT_INVOCABLE_VAR_0
  - TOOL_RESULT_COORDINATOR_MCP_PROMPT_NOT_INVOCABLE_VAR_1
-->
"/${TOOL_RESULT_COORDINATOR_MCP_PROMPT_NOT_INVOCABLE_VAR_0(TOOL_RESULT_COORDINATOR_MCP_PROMPT_NOT_INVOCABLE_VAR_1.name)}" is an MCP prompt and cannot run in coordinator mode: the coordinator does not load prompt content, and workers cannot invoke MCP prompts via the ${TOOL_RESULT_COORDINATOR_MCP_PROMPT_NOT_INVOCABLE_VAR_2} tool.
