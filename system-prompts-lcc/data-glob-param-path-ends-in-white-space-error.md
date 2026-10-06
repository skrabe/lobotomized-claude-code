<!--
name: 'Data: Path param ends in white space error'
description: >-
  Validation error telling Claude that a path parameter ends in white space once
  '.' and '..' are resolved, which the tool refuses, asking it to resend the
  path without the white space
ccVersion: 2.1.291
variables:
  - DATA_GLOB_PARAM_PATH_ENDS_IN_WHITE_SPACE_ERROR_VAR_0
  - DATA_GLOB_PARAM_PATH_ENDS_IN_WHITE_SPACE_ERROR_VAR_1
-->
${DATA_GLOB_PARAM_PATH_ENDS_IN_WHITE_SPACE_ERROR_VAR_0} ${DATA_GLOB_PARAM_PATH_ENDS_IN_WHITE_SPACE_ERROR_VAR_1[0]} ends in white space once its "." and ".." are resolved, and ${DATA_GLOB_PARAM_PATH_ENDS_IN_WHITE_SPACE_ERROR_VAR_0} refuses such a path. If the white space is not meant, send the path without it. ${DATA_GLOB_PARAM_PATH_ENDS_IN_WHITE_SPACE_ERROR_VAR_0} cannot open a file whose own name ends in white space.
