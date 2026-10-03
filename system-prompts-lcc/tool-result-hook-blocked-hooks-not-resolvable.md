<!--
name: 'Tool Result: Hook blocked hooks not resolvable'
description: >-
  Blocking error when Claude Code cannot work out which hooks apply to a call,
  telling it to retry with different input or check the configured hooks.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_HOOK_BLOCKED_HOOKS_NOT_RESOLVABLE_VAR_0
  - TOOL_RESULT_HOOK_BLOCKED_HOOKS_NOT_RESOLVABLE_VAR_1
  - TOOL_RESULT_HOOK_BLOCKED_HOOKS_NOT_RESOLVABLE_VAR_2
-->
Blocked: Claude Code could not work out which hooks apply to this call. Retry with a different input. If every call is blocked, check the ${TOOL_RESULT_HOOK_BLOCKED_HOOKS_NOT_RESOLVABLE_VAR_0} hooks in /hooks or in your settings.${TOOL_RESULT_HOOK_BLOCKED_HOOKS_NOT_RESOLVABLE_VAR_1===void 0?"":` (${TOOL_RESULT_HOOK_BLOCKED_HOOKS_NOT_RESOLVABLE_VAR_2(TOOL_RESULT_HOOK_BLOCKED_HOOKS_NOT_RESOLVABLE_VAR_1)})`}
