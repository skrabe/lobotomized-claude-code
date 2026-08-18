<!--
name: SendMessage local session identity notes
description: >-
  Parenthetical identity notes appended when messaging a local session that is
  also on Remote Control or has a remote namesake.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_SEND_MESSAGE_LOCAL_SESSION_IDENTITY_NOTES_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_LOCAL_SESSION_IDENTITY_NOTES_VAR_1
-->
${TOOL_RESULT_SEND_MESSAGE_LOCAL_SESSION_IDENTITY_NOTES_VAR_0.alsoListedRemotely?"; it is also connected via Remote Control":""}${TOOL_RESULT_SEND_MESSAGE_LOCAL_SESSION_IDENTITY_NOTES_VAR_0.remoteNamesakeClaimedLocally?`; a Remote Control or cloud session also named '${TOOL_RESULT_SEND_MESSAGE_LOCAL_SESSION_IDENTITY_NOTES_VAR_0.displayName}' is registered to a session on this machine`:""}${TOOL_RESULT_SEND_MESSAGE_LOCAL_SESSION_IDENTITY_NOTES_VAR_0.searchTruncated?TOOL_RESULT_SEND_MESSAGE_LOCAL_SESSION_IDENTITY_NOTES_VAR_1:""}
