<!--
name: 'Remote Tool: Bridge Ask Cannot Prompt'
description: >-
  Refusal when a session ask-rule on the bridge fires but this context cannot
  show a permission prompt (dontAsk / no prompts).
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_TOOL_BRIDGE_ASK_CANNOT_PROMPT_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_BRIDGE_ASK_CANNOT_PROMPT_VAR_1
-->
The rule ${TOOL_RESULT_REMOTE_TOOL_BRIDGE_ASK_CANNOT_PROMPT_VAR_0} asks before this session uses the bridge that reaches ${TOOL_RESULT_REMOTE_TOOL_BRIDGE_ASK_CANNOT_PROMPT_VAR_1.name}, and this context cannot ask.
