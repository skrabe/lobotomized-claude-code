<!--
name: 'Tool result: auto mode unavailable server check off for session'
description: >-
  Deny message saying auto mode's server-side safety check does not run for this
  session, so the tool was not run.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_AUTO_MODE_UNAVAILABLE_SERVER_CHECK_OFF_FOR_SESSION_VAR_0
  - TOOL_RESULT_AUTO_MODE_UNAVAILABLE_SERVER_CHECK_OFF_FOR_SESSION_VAR_1
  - TOOL_RESULT_AUTO_MODE_UNAVAILABLE_SERVER_CHECK_OFF_FOR_SESSION_VAR_2
-->
Auto mode is unavailable: its safety check does not run for this session, so ${TOOL_RESULT_AUTO_MODE_UNAVAILABLE_SERVER_CHECK_OFF_FOR_SESSION_VAR_0.name} was not run. The check runs on the server, and ${TOOL_RESULT_AUTO_MODE_UNAVAILABLE_SERVER_CHECK_OFF_FOR_SESSION_VAR_1}. This is not a judgment that the action is unsafe. Other actions that need the check will be denied too, and retrying won't help. Finish what you can without them, then stop and ${TOOL_RESULT_AUTO_MODE_UNAVAILABLE_SERVER_CHECK_OFF_FOR_SESSION_VAR_2?"report what is blocked and why. A new agent or a new conversation may get the check back. Don't change permission rules, settings or the permission mode yourself.":"tell the user what is blocked and why. Also tell them that they can start a new conversation (/clear), compact this one (/compact), or switch to another permission mode. These choices are the user's: don't change permission rules, settings or the permission mode yourself."}
