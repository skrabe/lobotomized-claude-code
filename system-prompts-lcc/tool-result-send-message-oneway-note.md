<!--
name: 'Tool Result: SendMessage one-way note'
description: >-
  Notes the send is one-way so the receiver cannot address a reply to this
  session
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_SEND_MESSAGE_ONEWAY_NOTE_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_ONEWAY_NOTE_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_ONEWAY_NOTE_VAR_2
  - TOOL_RESULT_SEND_MESSAGE_ONEWAY_NOTE_VAR_3
-->
; one-way: ${TOOL_RESULT_SEND_MESSAGE_ONEWAY_NOTE_VAR_0(TOOL_RESULT_SEND_MESSAGE_ONEWAY_NOTE_VAR_1)}, so the receiver cannot address a reply to this session${TOOL_RESULT_SEND_MESSAGE_ONEWAY_NOTE_VAR_2?`${TOOL_RESULT_SEND_MESSAGE_ONEWAY_NOTE_VAR_1==="rc-disconnected"?" (a reply needs Remote Control on here, and usually your user's permission too)":""} — ${TOOL_RESULT_SEND_MESSAGE_ONEWAY_NOTE_VAR_3}`:""}
