<!--
name: Permission objections exceed limits
description: >-
  Requests smaller calls or paths when objections cannot be presented to the
  user.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_TOOL_PERMISSION_OBJECTIONS_TOO_LARGE_VAR_0
  - TOOL_RESULT_SERVED_TOOL_PERMISSION_OBJECTIONS_TOO_LARGE_VAR_1
-->
${TOOL_RESULT_SERVED_TOOL_PERMISSION_OBJECTIONS_TOO_LARGE_VAR_0.name} was not run: the permission check's objections are too many, or one is too long, to put to the user, so nobody was asked. Send smaller calls, or use shorter paths. The check said: ${TOOL_RESULT_SERVED_TOOL_PERMISSION_OBJECTIONS_TOO_LARGE_VAR_1.message}
