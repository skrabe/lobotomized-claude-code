<!--
name: 'Tool Result: SendUserFile not a plain zip'
description: >-
  Refusal when a file could not be read as a plain zip, so it could not be
  checked; tells to rebuild with zip -r.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_SEND_USER_FILE_NOT_PLAIN_ZIP_VAR_0
  - TOOL_RESULT_SEND_USER_FILE_NOT_PLAIN_ZIP_VAR_1
  - TOOL_RESULT_SEND_USER_FILE_NOT_PLAIN_ZIP_VAR_2
-->
${TOOL_RESULT_SEND_USER_FILE_NOT_PLAIN_ZIP_VAR_0}${TOOL_RESULT_SEND_USER_FILE_NOT_PLAIN_ZIP_VAR_1} could not be read as a plain zip file, so its files could not be checked for secret keys. Make it again with \`zip -r\`, as in step 4 of ${TOOL_RESULT_SEND_USER_FILE_NOT_PLAIN_ZIP_VAR_2}, and send that.
