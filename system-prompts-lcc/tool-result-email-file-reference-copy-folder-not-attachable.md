<!--
name: 'Tool result: email file reference outside copy folder'
description: >-
  Refusal: files under the given folder can't be attached by reference; files in
  the copy folder can.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_COPY_FOLDER_NOT_ATTACHABLE_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_COPY_FOLDER_NOT_ATTACHABLE_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_COPY_FOLDER_NOT_ATTACHABLE_VAR_2
-->
Nothing was sent to ${TOOL_RESULT_EMAIL_FILE_REFERENCE_COPY_FOLDER_NOT_ATTACHABLE_VAR_0.serviceName}: files under ${TOOL_RESULT_EMAIL_FILE_REFERENCE_COPY_FOLDER_NOT_ATTACHABLE_VAR_1.copy.from} can't be attached by reference. Files in ${TOOL_RESULT_EMAIL_FILE_REFERENCE_COPY_FOLDER_NOT_ATTACHABLE_VAR_2(TOOL_RESULT_EMAIL_FILE_REFERENCE_COPY_FOLDER_NOT_ATTACHABLE_VAR_1.copy.into)} can, if nothing else refuses them.
