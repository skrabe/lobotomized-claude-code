<!--
name: 'Tool Result: FetchInboxMessage Wrong Session'
description: >-
  FetchInboxMessage tool_result when the stored message names a different
  session, so it was not read.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_FETCH_INBOX_MESSAGE_WRONG_SESSION_VAR_0
-->
No inbox message at ${TOOL_RESULT_FETCH_INBOX_MESSAGE_WRONG_SESSION_VAR_0.file_id??"that id"} for this session (it names a different session, so it was not read).
