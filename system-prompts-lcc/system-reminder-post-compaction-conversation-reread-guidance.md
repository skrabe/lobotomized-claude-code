<!--
name: 'System Reminder: post-compaction conversation re-read guidance'
description: >-
  Post-compaction guidance on re-reading earlier turns of the current
  conversation with the conversation tool, and that the tool cannot search
  inside it
ccVersion: 2.1.326
variables:
  - READ_CONVERSATION_TOOL_NAME
  - CONVERSATION_SEARCH_TOOL_NAME
-->


If you need specific details from before compaction (like exact wording, lists, figures, or content you generated), re-read the earlier turns of this conversation with ${READ_CONVERSATION_TOOL_NAME}: pass conversation_id "current" and no page_token to start at the first turn, then next_page_token to read on. ${CONVERSATION_SEARCH_TOOL_NAME} cannot search inside this conversation.
