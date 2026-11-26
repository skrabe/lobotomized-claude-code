<!--
name: 'Unlinked chat: further call note'
description: >-
  Tool result for a repeat call in an unlinked chat, with the one-time search
  rule for computer tools.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_COMPUTER_USE_UNLINKED_CHAT_FURTHER_CALL_VAR_0
  - TOOL_RESULT_COMPUTER_USE_UNLINKED_CHAT_FURTHER_CALL_VAR_1
  - TOOL_RESULT_COMPUTER_USE_UNLINKED_CHAT_FURTHER_CALL_VAR_2
-->
This chat isn't linked to a computer right now, and ${TOOL_RESULT_COMPUTER_USE_UNLINKED_CHAT_FURTHER_CALL_VAR_0}. ${TOOL_RESULT_COMPUTER_USE_UNLINKED_CHAT_FURTHER_CALL_VAR_1} There is one time to look: if the user's next message is only "Continue" or the name of a computer and you see no tools whose names start with mcp__${TOOL_RESULT_COMPUTER_USE_UNLINKED_CHAT_FURTHER_CALL_VAR_2}__, search for them once first, because they can take a moment to arrive. If the user asks again for something that needs their computer, a new call can bring a new card.
