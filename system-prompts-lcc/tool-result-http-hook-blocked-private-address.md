<!--
name: 'Tool Result: HTTP hook blocked private address'
description: >-
  Error when an HTTP hook target is not a public address, noting loopback is
  allowed for local dev
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_HTTP_HOOK_BLOCKED_PRIVATE_ADDRESS_VAR_0
  - TOOL_RESULT_HTTP_HOOK_BLOCKED_PRIVATE_ADDRESS_VAR_1
-->
HTTP hook blocked: ${TOOL_RESULT_HTTP_HOOK_BLOCKED_PRIVATE_ADDRESS_VAR_0===TOOL_RESULT_HTTP_HOOK_BLOCKED_PRIVATE_ADDRESS_VAR_1?`${TOOL_RESULT_HTTP_HOOK_BLOCKED_PRIVATE_ADDRESS_VAR_1} is not a public address`:`${TOOL_RESULT_HTTP_HOOK_BLOCKED_PRIVATE_ADDRESS_VAR_0} resolves to ${TOOL_RESULT_HTTP_HOOK_BLOCKED_PRIVATE_ADDRESS_VAR_1} (private/link-local address)`}. Loopback (127.0.0.1, ::1) is allowed for local dev.
