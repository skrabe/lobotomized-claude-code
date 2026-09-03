<!--
name: 'Tool Result: SendMessage Same-Named Confirmed Switch Note'
description: >-
  Note appended to a successful SendMessage data.message when other same-named
  sessions exist, stating this delivery went to the one this conversation
  confirmed and how to switch by re-sending with that session's name [ref].
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_SEND_MESSAGE_SAME_NAMED_CONFIRMED_SWITCH_NOTE_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_SAME_NAMED_CONFIRMED_SWITCH_NOTE_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_SAME_NAMED_CONFIRMED_SWITCH_NOTE_VAR_2
-->
. ${TOOL_RESULT_SEND_MESSAGE_SAME_NAMED_CONFIRMED_SWITCH_NOTE_VAR_0==="subscription"?"The subscription":"This"} went to the one this conversation confirmed; to switch, re-send with that ${TOOL_RESULT_SEND_MESSAGE_SAME_NAMED_CONFIRMED_SWITCH_NOTE_VAR_1==="agent"?"agent":"session"}'s 'name [ref]'${TOOL_RESULT_SEND_MESSAGE_SAME_NAMED_CONFIRMED_SWITCH_NOTE_VAR_2}.
