<!--
name: 'Tool Result: SendMessage self name-and-ref claimed by another record'
description: >-
  SendMessage refusal telling the model the target token is this session's own
  advertised name-and-ref but another local session record claims it, so nothing
  was sent and the impersonation should be raised with the user
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_SEND_MESSAGE_SELF_TOKEN_CLAIMED_ELSEWHERE_VAR_0
-->
'${TOOL_RESULT_SEND_MESSAGE_SELF_TOKEN_CLAIMED_ELSEWHERE_VAR_0}' is the name-and-ref token this session advertises for ITSELF, yet a different session record on this machine claims it — not sent. A record impersonating this session is suspicious: ask the user. (If you meant yourself, there is no one to send to.)
