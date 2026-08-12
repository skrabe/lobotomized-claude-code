<!--
name: Same-named agent note
description: >-
  Note appended to the SendMessage model tool result about other same-named
  agents.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_SEND_MESSAGE_SAMENAME_AGENT_NOTE_VAR_0
-->

Note: ${TOOL_RESULT_SEND_MESSAGE_SAMENAME_AGENT_NOTE_VAR_0.sameNamedSiblings} other agent${TOOL_RESULT_SEND_MESSAGE_SAMENAME_AGENT_NOTE_VAR_0.sameNamedSiblings===1?" is":"s are"} also named '${TOOL_RESULT_SEND_MESSAGE_SAMENAME_AGENT_NOTE_VAR_0.displayName}'. This went to the one this conversation confirmed; to switch, re-send with that agent's 'name [ref]'${TOOL_RESULT_SEND_MESSAGE_SAMENAME_AGENT_NOTE_VAR_1?` (${TOOL_RESULT_SEND_MESSAGE_SAMENAME_AGENT_NOTE_VAR_2} lists them)`:""}.
