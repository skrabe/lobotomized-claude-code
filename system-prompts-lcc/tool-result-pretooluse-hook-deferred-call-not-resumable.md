<!--
name: 'Tool Result: PreToolUse hook deferred call not resumable'
description: >-
  Tells the model a PreToolUse hook deferred the call but a script-originated
  call cannot be resumed, so it did not run
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_PRETOOLUSE_HOOK_DEFERRED_CALL_NOT_RESUMABLE_VAR_0
  - TOOL_RESULT_PRETOOLUSE_HOOK_DEFERRED_CALL_NOT_RESUMABLE_VAR_1
-->
A PreToolUse hook (${TOOL_RESULT_PRETOOLUSE_HOOK_DEFERRED_CALL_NOT_RESUMABLE_VAR_0}) deferred this call. ${TOOL_RESULT_PRETOOLUSE_HOOK_DEFERRED_CALL_NOT_RESUMABLE_VAR_1!==void 0?`A call from a background script can't be resumed later, so it did not run. To make such calls resumable, the app's developer can add "${TOOL_RESULT_PRETOOLUSE_HOOK_DEFERRED_CALL_NOT_RESUMABLE_VAR_1}" to disallowedTools.`:"A call from a script can't be resumed later, so it did not run."}
