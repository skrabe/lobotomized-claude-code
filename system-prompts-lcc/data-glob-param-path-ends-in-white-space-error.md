<!--
name: 'Data: Glob param path ends in white space error'
description: >-
  Validation error telling Claude that a path parameter ends in white space once
  '.' and '..' are resolved and so does not name one file, asking it to remove
  the white space and retry
ccVersion: 2.1.288
variables:
  - DATA_GLOB_PARAM_PATH_ENDS_IN_WHITE_SPACE_ERROR_VAR_0
  - DATA_GLOB_PARAM_PATH_ENDS_IN_WHITE_SPACE_ERROR_VAR_1
-->
${DATA_GLOB_PARAM_PATH_ENDS_IN_WHITE_SPACE_ERROR_VAR_0} ${DATA_GLOB_PARAM_PATH_ENDS_IN_WHITE_SPACE_ERROR_VAR_1[0]} ends in white space once its "." and ".." are resolved, so it does not name one file. Remove that white space, or what follows it, and try again.
