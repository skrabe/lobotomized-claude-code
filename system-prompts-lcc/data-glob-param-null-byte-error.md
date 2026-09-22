<!--
name: 'Data: Glob/Grep param null byte error'
description: >-
  tool_result validation error returned to the model when a Glob/Grep param
  contains a null byte.
ccVersion: 2.1.178
variables:
  - DATA_GLOB_PARAM_NULL_BYTE_ERROR_VAR_0
  - DATA_GLOB_PARAM_NULL_BYTE_ERROR_VAR_1
-->
${DATA_GLOB_PARAM_NULL_BYTE_ERROR_VAR_0} ${DATA_GLOB_PARAM_NULL_BYTE_ERROR_VAR_1[0]} cannot contain null bytes (\\0). Remove the null byte and try again.
