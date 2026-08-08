<!--
name: 'Tool Parameter: SendMessage Recipient (Cross-Session)'
description: >-
  zod .describe() for SendMessage's `to` parameter in the cross-session build,
  naming the listing/[ref]/teammate/main/agentId address forms.
ccVersion: 2.1.224
variables:
  - TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_0
-->
Recipient: a name from ${TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_0} (append its " [ref]" only when a listing or an error shows one), a teammate name, "main", or a background agent's agentId
