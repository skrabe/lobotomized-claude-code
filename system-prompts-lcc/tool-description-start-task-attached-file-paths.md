<!--
name: Start task attached file paths
description: Explains how to pass chat attachments to start_task using full paths.
ccVersion: 2.1.294
variables:
  - TOOL_DESCRIPTION_START_TASK_ATTACHED_FILE_PATHS_VAR_0
-->
In this session, files the user attached to the chat are usually in ${TOOL_DESCRIPTION_START_TASK_ATTACHED_FILE_PATHS_VAR_0}. To give one to the task, put its full path in files as an object, such as files: [{"path": "${TOOL_DESCRIPTION_START_TASK_ATTACHED_FILE_PATHS_VAR_0}/report.csv"}]. Do that rather than copying the file's text into task_description.
