<!--
name: 'Tool Result: SendUserFile upload limit reached'
description: Lists files not uploaded because the account hit its upload limit.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_REACHED_VAR_0
  - TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_REACHED_VAR_1
-->
${TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_REACHED_VAR_0.length} ${TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_REACHED_VAR_1(TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_REACHED_VAR_0.length,"file")} not uploaded, because this account has uploaded as many files as it is allowed for now:
