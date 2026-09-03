<!--
name: PreToolUse Hook Served Call Gate Refused
description: >-
  PreToolUse blockingError rewritten as a permission deny when a served-call
  hook timed out or could not render a verdict.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_PRETOOLUSE_HOOK_SERVED_CALL_GATE_REFUSED_VAR_0
  - TOOL_RESULT_PRETOOLUSE_HOOK_SERVED_CALL_GATE_REFUSED_VAR_1
-->
a PreToolUse ${TOOL_RESULT_PRETOOLUSE_HOOK_SERVED_CALL_GATE_REFUSED_VAR_0.hook.type} hook here ${TOOL_RESULT_PRETOOLUSE_HOOK_SERVED_CALL_GATE_REFUSED_VAR_1} for a call served for a cloud session; refusing rather than skipping that gate
