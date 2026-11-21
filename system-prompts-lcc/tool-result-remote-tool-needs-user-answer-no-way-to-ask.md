<!--
name: 'Tool Result: Remote tool needs answer, no way to ask'
description: >-
  Tells Claude a call did not run because the session had no way to ask the
  user, and to ask rather than retry
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_REMOTE_TOOL_NEEDS_USER_ANSWER_NO_WAY_TO_ASK_VAR_0
-->
This call did not run: it needs the user's answer, and this session had no way to ask. ${TOOL_RESULT_REMOTE_TOOL_NEEDS_USER_ANSWER_NO_WAY_TO_ASK_VAR_0} Ask the user how to proceed rather than retrying.
