<!--
name: Server interface version refusal
description: Reports an unreadable or incompatible caller interface version.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_TOOL_INTERFACE_VERSION_REFUSAL_VAR_0
  - TOOL_RESULT_SERVED_TOOL_INTERFACE_VERSION_REFUSAL_VAR_1
  - TOOL_RESULT_SERVED_TOOL_INTERFACE_VERSION_REFUSAL_VAR_2
  - TOOL_RESULT_SERVED_TOOL_INTERFACE_VERSION_REFUSAL_VAR_3
-->
${TOOL_RESULT_SERVED_TOOL_INTERFACE_VERSION_REFUSAL_VAR_0} was not run: ${TOOL_RESULT_SERVED_TOOL_INTERFACE_VERSION_REFUSAL_VAR_1===void 0?"this server could not read the version of the interface that its caller stated with the call":TOOL_RESULT_SERVED_TOOL_INTERFACE_VERSION_REFUSAL_VAR_2==="session_too_old"?`this session speaks version ${TOOL_RESULT_SERVED_TOOL_INTERFACE_VERSION_REFUSAL_VAR_1.version} of the interface to this server, which works with version ${TOOL_RESULT_SERVED_TOOL_INTERFACE_VERSION_REFUSAL_VAR_3.min_version} or later`:`this session works with version ${TOOL_RESULT_SERVED_TOOL_INTERFACE_VERSION_REFUSAL_VAR_1.min_version} or later of the interface to this server, which speaks version ${TOOL_RESULT_SERVED_TOOL_INTERFACE_VERSION_REFUSAL_VAR_3.version}`}. Retrying won't help: tell the user.
