<!--
name: 'Data: Working directory cannot be resolved'
description: >-
  Reason that the working directory cannot be resolved, with the error code when
  known
ccVersion: 2.1.330
variables:
  - DATA_WORKING_DIRECTORY_CANNOT_BE_RESOLVED_VAR_0
  - DATA_WORKING_DIRECTORY_CANNOT_BE_RESOLVED_VAR_1
-->
${DATA_WORKING_DIRECTORY_CANNOT_BE_RESOLVED_VAR_0==="person"?"couldn't":"can't"} be resolved${DATA_WORKING_DIRECTORY_CANNOT_BE_RESOLVED_VAR_1.code===void 0?"":` (error ${DATA_WORKING_DIRECTORY_CANNOT_BE_RESOLVED_VAR_1.code})`}
