<!--
name: Output protocol version mismatch
description: Reports incompatible output object protocol versions.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_TOOL_OUTPUT_NO_SHARED_VERSION_VAR_0
  - TOOL_RESULT_SERVED_TOOL_OUTPUT_NO_SHARED_VERSION_VAR_1
  - TOOL_RESULT_SERVED_TOOL_OUTPUT_NO_SHARED_VERSION_VAR_2
-->
${TOOL_RESULT_SERVED_TOOL_OUTPUT_NO_SHARED_VERSION_VAR_0} was not run: this server returns output objects only in version ${TOOL_RESULT_SERVED_TOOL_OUTPUT_NO_SHARED_VERSION_VAR_1.join(", ")}, and the request lists ${TOOL_RESULT_SERVED_TOOL_OUTPUT_NO_SHARED_VERSION_VAR_2.versions.join(", ")||"none"}.
