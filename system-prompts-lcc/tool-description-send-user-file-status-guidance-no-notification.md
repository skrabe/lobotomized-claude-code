<!--
name: 'Tool Description: SendUserFile status guidance (no notification)'
description: >-
  SendUserFile prompt variant telling the model to set status on every call,
  when to use proactive versus normal, that neither sends a notification, and to
  also call the notify tool when the run should notify the user
ccVersion: 2.1.325
variables:
  - TOOL_DESCRIPTION_SEND_USER_FILE_STATUS_GUIDANCE_NO_NOTIFICATION_VAR_0
-->
Set \`status\` on every call. Use \`proactive\` when you're initiating (build artifact ready, report generated). Use \`normal\` when replying to something the user just said. Neither one sends a notification: the file waits in this session until the user opens it. If this run is meant to notify the user, call ${TOOL_DESCRIPTION_SEND_USER_FILE_STATUS_GUIDANCE_NO_NOTIFICATION_VAR_0} as well.
