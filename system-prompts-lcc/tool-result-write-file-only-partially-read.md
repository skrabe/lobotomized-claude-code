<!--
name: 'Tool Result: Write refused on partially read file'
description: >-
  Write tool validation error when not all of the file was read in one call,
  telling Claude to Read it whole (with the full-read parameter) or use Edit
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_WRITE_FILE_ONLY_PARTIALLY_READ_VAR_0
  - TOOL_RESULT_WRITE_FILE_ONLY_PARTIALLY_READ_VAR_1
  - TOOL_RESULT_WRITE_FILE_ONLY_PARTIALLY_READ_VAR_2
  - TOOL_RESULT_WRITE_FILE_ONLY_PARTIALLY_READ_VAR_3
-->
Nothing was written. Nothing shows that you have read all of this file in one call, so a ${TOOL_RESULT_WRITE_FILE_ONLY_PARTIALLY_READ_VAR_0} could lose text that you have not seen. First ${TOOL_RESULT_WRITE_FILE_ONLY_PARTIALLY_READ_VAR_1} it in one call with no offset or limit. If ${TOOL_RESULT_WRITE_FILE_ONLY_PARTIALLY_READ_VAR_1} returns only a page or says the file is too large, ${TOOL_RESULT_WRITE_FILE_ONLY_PARTIALLY_READ_VAR_1} it again with ${TOOL_RESULT_WRITE_FILE_ONLY_PARTIALLY_READ_VAR_2}: true. If that cannot return all of it, or a ${TOOL_RESULT_WRITE_FILE_ONLY_PARTIALLY_READ_VAR_0} is still refused, use ${TOOL_RESULT_WRITE_FILE_ONLY_PARTIALLY_READ_VAR_3}.
