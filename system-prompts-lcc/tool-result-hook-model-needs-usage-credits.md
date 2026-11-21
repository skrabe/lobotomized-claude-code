<!--
name: 'Tool Result: Hook model needs usage credits'
description: >-
  Explains that a prompt/agent hook's model requires usage credits and no
  fallback model may run it, with how to fix it
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_HOOK_MODEL_NEEDS_USAGE_CREDITS_VAR_0
  - TOOL_RESULT_HOOK_MODEL_NEEDS_USAGE_CREDITS_VAR_1
  - TOOL_RESULT_HOOK_MODEL_NEEDS_USAGE_CREDITS_VAR_2
-->
${TOOL_RESULT_HOOK_MODEL_NEEDS_USAGE_CREDITS_VAR_0(TOOL_RESULT_HOOK_MODEL_NEEDS_USAGE_CREDITS_VAR_1)} requires usage credits and ${TOOL_RESULT_HOOK_MODEL_NEEDS_USAGE_CREDITS_VAR_2.CLAUDE_CODE_NO_MODEL_FALLBACK===!0?"CLAUDE_CODE_NO_MODEL_FALLBACK lets no other model":"no other model may"} run this hook · set up usage credits with /model, or give the hook another model
