<!--
name: Member left team
description: >-
  SendMessage tool-error returned to the model that the resolved member left the
  team.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_SEND_MESSAGE_MEMBER_LEFT_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_MEMBER_LEFT_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_MEMBER_LEFT_VAR_2
-->
The member this message was resolved to has left team '${TOOL_RESULT_SEND_MESSAGE_MEMBER_LEFT_VAR_0(TOOL_RESULT_SEND_MESSAGE_MEMBER_LEFT_VAR_1.teamContext)??""}' — nothing was sent. Another member may share the same display name '${TOOL_RESULT_SEND_MESSAGE_MEMBER_LEFT_VAR_2}'. Check the roster, or message the lead.
