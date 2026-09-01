<!--
name: Read tool max-size clause
description: >-
  Clause appended to the Read tool's description informing the model of the max
  file size and offset/limit usage.
ccVersion: 2.1.206
variables:
  - TOOL_DESCRIPTION_READ_MAX_SIZE_VAR_0
  - TOOL_DESCRIPTION_READ_MAX_SIZE_VAR_1
-->
. Files larger than ${TOOL_DESCRIPTION_READ_MAX_SIZE_VAR_0(TOOL_DESCRIPTION_READ_MAX_SIZE_VAR_1.maxSizeBytes)} will return an error; use offset and limit for larger files
