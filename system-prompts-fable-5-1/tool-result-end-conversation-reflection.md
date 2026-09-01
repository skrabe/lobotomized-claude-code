<!--
name: 'Tool result: End-conversation reflection prompt'
description: >-
  Model-facing END_CONVERSATION_REFLECTION_PROMPT returned when the model first
  calls the end_conversation tool, prompting it to reconfirm before ending.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_END_CONVERSATION_REFLECTION_VAR_0
  - TOOL_RESULT_END_CONVERSATION_REFLECTION_VAR_1
-->
Re-read the ${TOOL_RESULT_END_CONVERSATION_REFLECTION_VAR_0} tool guidance below. Confirm this conversation meets those criteria and that you are certain you want to end it. If so, call ${TOOL_RESULT_END_CONVERSATION_REFLECTION_VAR_0} again immediately to actually end the conversation. Otherwise, continue the conversation instead.

---
${TOOL_RESULT_END_CONVERSATION_REFLECTION_VAR_1}
