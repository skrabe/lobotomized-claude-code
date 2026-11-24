<!--
name: 'Tool Parameter: SendMessage Recipient (Cross-Session)'
description: >-
  zod .describe() for SendMessage's `to` parameter in the cross-session build,
  naming the listing/[ref]/teammate/main/agentId address forms.
ccVersion: 2.1.331
variables:
  - TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_0
  - TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_1
  - TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_2
  - TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_3
  - TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_4
-->
Recipient: a name from ${TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_0} (append its " [ref]" only when a listing or an error shows one), a teammate name, "main", or a background agent's agentId${TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_1?`; the session id of another cloud or Remote Control session; or "${TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_2}", the session that created this one`:""}${TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_3?`; "${TOOL_PARAMETER_SENDMESSAGE_RECIPIENT_CROSS_SESSION_VAR_4}" sends nothing and finds sessions by title`:""}
