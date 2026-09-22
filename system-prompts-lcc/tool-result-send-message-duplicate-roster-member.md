<!--
name: 'Tool Result: Duplicate roster member on send'
description: >-
  Model-facing tool_result returned when the team roster lists the resolved
  recipient more than once, so the message was not sent.
ccVersion: 2.1.199
variables:
  - TOOL_RESULT_SEND_MESSAGE_DUPLICATE_ROSTER_MEMBER_VAR_0
-->
The team roster lists the member this message was resolved to more than once — nothing was sent. Ask the lead to repair team '${TOOL_RESULT_SEND_MESSAGE_DUPLICATE_ROSTER_MEMBER_VAR_0}''s file.
