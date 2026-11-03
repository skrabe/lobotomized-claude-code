<!--
name: 'Tool Result: project_write read local_path first'
description: Read the whole file first (again if edited) or pass its text as content
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_PROJECT_WRITE_LOCALPATH_SESSION_READ_FIRST_VAR_0
  - TOOL_RESULT_PROJECT_WRITE_LOCALPATH_SESSION_READ_FIRST_VAR_1
-->
project_write: Read the whole file at local_path first (again, if you read, wrote or edited it earlier in this chat), or pass its text as content.${TOOL_RESULT_PROJECT_WRITE_LOCALPATH_SESSION_READ_FIRST_VAR_0()?` If it is an unchanged copy of a file that you wrote with ${TOOL_RESULT_PROJECT_WRITE_LOCALPATH_SESSION_READ_FIRST_VAR_1}, pass the path at which you wrote it.`:""}
