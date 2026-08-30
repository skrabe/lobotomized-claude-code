<!--
name: Eval Mock Stand-In Tool-Error Format
description: >-
  Tells the plugin-eval mock MCP stand-in model to emit a one-line ERROR: prefix
  for ordinary tool errors the agent under test should handle.
ccVersion: 2.1.251
variables:
  - AGENT_PROMPT_EVAL_MOCK_STAND_IN_ERROR_FORMAT_VAR_0
-->
To return an ordinary tool ERROR the agent should handle (bad arguments, not found, rate limited), reply with a single line starting "${AGENT_PROMPT_EVAL_MOCK_STAND_IN_ERROR_FORMAT_VAR_0} " followed by the error text.
