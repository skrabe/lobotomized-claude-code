<!--
name: PreToolUse hook invalid updatedInput
description: >-
  Hook deny message returned to the model when a PreToolUse hook's updatedInput
  fails schema validation.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_PRETOOLUSE_HOOK_INVALID_INPUT_VAR_0
  - TOOL_RESULT_PRETOOLUSE_HOOK_INVALID_INPUT_VAR_1
  - TOOL_RESULT_PRETOOLUSE_HOOK_INVALID_INPUT_VAR_2
-->
PreToolUse hook for ${TOOL_RESULT_PRETOOLUSE_HOOK_INVALID_INPUT_VAR_0.name} returned updatedInput that failed schema validation: ${TOOL_RESULT_PRETOOLUSE_HOOK_INVALID_INPUT_VAR_1(TOOL_RESULT_PRETOOLUSE_HOOK_INVALID_INPUT_VAR_0.name,TOOL_RESULT_PRETOOLUSE_HOOK_INVALID_INPUT_VAR_2)}
