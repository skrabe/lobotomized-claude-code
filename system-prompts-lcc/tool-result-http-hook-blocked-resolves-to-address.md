<!--
name: 'Tool result: HTTP hook blocked resolved address'
description: >-
  HTTP hook block reason naming the host and the private/link-local or
  unreachable address it resolves to
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_HTTP_HOOK_BLOCKED_RESOLVES_TO_ADDRESS_VAR_0
  - TOOL_RESULT_HTTP_HOOK_BLOCKED_RESOLVES_TO_ADDRESS_VAR_1
  - TOOL_RESULT_HTTP_HOOK_BLOCKED_RESOLVES_TO_ADDRESS_VAR_2
-->
${TOOL_RESULT_HTTP_HOOK_BLOCKED_RESOLVES_TO_ADDRESS_VAR_0} resolves to ${TOOL_RESULT_HTTP_HOOK_BLOCKED_RESOLVES_TO_ADDRESS_VAR_1}${TOOL_RESULT_HTTP_HOOK_BLOCKED_RESOLVES_TO_ADDRESS_VAR_2?" (private/link-local address)":", which HTTP hooks may not reach"}
