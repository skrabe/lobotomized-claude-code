<!--
name: SendUserFile files delivered tool_result
description: >-
  Model-facing SendUserFile tool_result confirming N file(s) were delivered to
  the user. 2.1.204 emission-shape change (subset-shadowed by the
  message-delivered result) dropped it from capture; force-restore.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_SENDUSERFILE_FILES_DELIVERED_VAR_0
  - TOOL_RESULT_SENDUSERFILE_FILES_DELIVERED_VAR_1
-->
${TOOL_RESULT_SENDUSERFILE_FILES_DELIVERED_VAR_0} ${TOOL_RESULT_SENDUSERFILE_FILES_DELIVERED_VAR_1(TOOL_RESULT_SENDUSERFILE_FILES_DELIVERED_VAR_0,"file")} delivered to user.
