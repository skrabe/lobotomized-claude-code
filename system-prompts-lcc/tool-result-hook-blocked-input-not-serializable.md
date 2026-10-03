<!--
name: 'Tool Result: Hook blocked input not serializable'
description: >-
  Blocking error when a call's input cannot be written as JSON for the hook
  check because it is too large or has non-JSON values, telling Claude to retry
  with smaller plain input.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_HOOK_BLOCKED_INPUT_NOT_SERIALIZABLE_VAR_0
  - TOOL_RESULT_HOOK_BLOCKED_INPUT_NOT_SERIALIZABLE_VAR_1
-->
Blocked: this call's input can't be written as JSON, so the hook could not check it. The input is too large, or contains a value that JSON can't represent (such as a BigInt or a circular reference). Retry with a smaller, plain input.${TOOL_RESULT_HOOK_BLOCKED_INPUT_NOT_SERIALIZABLE_VAR_0===void 0?"":` (JSON error: ${TOOL_RESULT_HOOK_BLOCKED_INPUT_NOT_SERIALIZABLE_VAR_1(TOOL_RESULT_HOOK_BLOCKED_INPUT_NOT_SERIALIZABLE_VAR_0)})`}
