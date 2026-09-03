<!--
name: SendMessage remote session identity notes
description: >-
  Parenthetical identity notes appended to the SendMessage result for a Remote
  Control or cloud recipient when a same-named session is registered locally or
  the search was truncated.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_SEND_MESSAGE_REMOTE_SESSION_IDENTITY_NOTES_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_REMOTE_SESSION_IDENTITY_NOTES_VAR_1
-->
${TOOL_RESULT_SEND_MESSAGE_REMOTE_SESSION_IDENTITY_NOTES_VAR_0.remoteNamesakeClaimedLocally?`; another session also named '${TOOL_RESULT_SEND_MESSAGE_REMOTE_SESSION_IDENTITY_NOTES_VAR_0.displayName}' is registered to a session on this machine`:""}${TOOL_RESULT_SEND_MESSAGE_REMOTE_SESSION_IDENTITY_NOTES_VAR_0.searchTruncated?TOOL_RESULT_SEND_MESSAGE_REMOTE_SESSION_IDENTITY_NOTES_VAR_1:""}
