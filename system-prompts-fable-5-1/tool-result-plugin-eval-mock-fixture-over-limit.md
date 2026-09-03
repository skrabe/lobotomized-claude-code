<!--
name: 'Tool Result: Plugin Eval Mock Fixture Over Size Limit'
description: 'Mock MCP tool_error when a {{file:…}} fixture exceeds the byte cap.'
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_PLUGIN_EVAL_MOCK_FIXTURE_OVER_LIMIT_VAR_0
  - TOOL_RESULT_PLUGIN_EVAL_MOCK_FIXTURE_OVER_LIMIT_VAR_1
-->
is ${TOOL_RESULT_PLUGIN_EVAL_MOCK_FIXTURE_OVER_LIMIT_VAR_0.size} bytes, over the ${TOOL_RESULT_PLUGIN_EVAL_MOCK_FIXTURE_OVER_LIMIT_VAR_1}-byte fixture limit
