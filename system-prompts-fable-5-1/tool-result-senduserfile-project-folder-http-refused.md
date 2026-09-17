<!--
name: 'Tool Result: SendUserFile Project Folder HTTP Refused'
description: >-
  SendUserFile project-folder upload error when the folder HTTP-refuses the
  file, interpolating the status/code.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_SENDUSERFILE_PROJECT_FOLDER_HTTP_REFUSED_VAR_0
-->
upload failed: the project folder refused the file (${(TOOL_RESULT_SENDUSERFILE_PROJECT_FOLDER_HTTP_REFUSED_VAR_0.code??`status ${TOOL_RESULT_SENDUSERFILE_PROJECT_FOLDER_HTTP_REFUSED_VAR_0.status}`).replaceAll("_"," ")})
