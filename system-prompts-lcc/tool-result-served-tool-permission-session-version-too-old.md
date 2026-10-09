<!--
name: Permission caller version too old
description: >-
  Explains that the caller permission interface version is older than the server
  minimum.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_TOOL_PERMISSION_SESSION_VERSION_TOO_OLD_VAR_0
  - TOOL_RESULT_SERVED_TOOL_PERMISSION_SESSION_VERSION_TOO_OLD_VAR_1
  - TOOL_RESULT_SERVED_TOOL_PERMISSION_SESSION_VERSION_TOO_OLD_VAR_2
-->
${TOOL_RESULT_SERVED_TOOL_PERMISSION_SESSION_VERSION_TOO_OLD_VAR_0} was not run: this session speaks version ${TOOL_RESULT_SERVED_TOOL_PERMISSION_SESSION_VERSION_TOO_OLD_VAR_1.session.version} of the interface to this server, which works with version ${TOOL_RESULT_SERVED_TOOL_PERMISSION_SESSION_VERSION_TOO_OLD_VAR_2.min_version} or later. Retrying won't help: tell the user.
