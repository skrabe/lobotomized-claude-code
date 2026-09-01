<!--
name: 'System Prompt: MCP resource text content wrapper'
description: >-
  Wraps an MCP text resource ('[Resource from X at uri] ' + body) into a
  tool_result text block the model reads
ccVersion: 2.1.178
variables:
  - SYSTEM_PROMPT_MCP_RESOURCE_TEXT_CONTENT_WRAPPER_VAR_0
  - SYSTEM_PROMPT_MCP_RESOURCE_TEXT_CONTENT_WRAPPER_VAR_1
-->
${SYSTEM_PROMPT_MCP_RESOURCE_TEXT_CONTENT_WRAPPER_VAR_0}${SYSTEM_PROMPT_MCP_RESOURCE_TEXT_CONTENT_WRAPPER_VAR_1.text}
