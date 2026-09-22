<!--
name: SendFile files-not-sent header
description: >-
  Header line in the SendFile tool result introducing the list of files that
  could not be sent.
ccVersion: 2.1.210
variables:
  - TOOL_RESULT_SENDFILE_FILES_NOT_SENT_HEADER_VAR_0
  - TOOL_RESULT_SENDFILE_FILES_NOT_SENT_HEADER_VAR_1
-->
${TOOL_RESULT_SENDFILE_FILES_NOT_SENT_HEADER_VAR_0.length} ${TOOL_RESULT_SENDFILE_FILES_NOT_SENT_HEADER_VAR_1(TOOL_RESULT_SENDFILE_FILES_NOT_SENT_HEADER_VAR_0.length,"file")} could NOT be sent:
