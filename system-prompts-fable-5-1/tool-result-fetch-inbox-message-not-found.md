<!--
name: 'Tool Result: FetchInboxMessage Not Found'
description: >-
  FetchInboxMessage tool_result when the id is unknown, belongs to another
  session, or has expired.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_FETCH_INBOX_MESSAGE_NOT_FOUND_VAR_0
-->
No inbox message at ${TOOL_RESULT_FETCH_INBOX_MESSAGE_NOT_FOUND_VAR_0.file_id??"that id"} for this session (unknown id, another session's message, or expired — messages are kept about a week).
