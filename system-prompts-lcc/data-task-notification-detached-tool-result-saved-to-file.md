<!--
name: 'Task Notification: Detached Tool Result Saved To File'
description: >-
  Task-notification result text telling the model that an oversized detached
  tool result was saved to a file (fully or truncated) and to read that file.
ccVersion: 2.1.277
variables:
  - DATA_TASK_NOTIFICATION_DETACHED_TOOL_RESULT_SAVED_TO_FILE_VAR_0
-->
The result is ${DATA_TASK_NOTIFICATION_DETACHED_TOOL_RESULT_SAVED_TO_FILE_VAR_0.originalSize} characters, too large to carry in a notification, so none of it is quoted here. ${DATA_TASK_NOTIFICATION_DETACHED_TOOL_RESULT_SAVED_TO_FILE_VAR_0.truncatedAtBytes===void 0?"All of it":`Its first ${DATA_TASK_NOTIFICATION_DETACHED_TOOL_RESULT_SAVED_TO_FILE_VAR_0.truncatedAtBytes} bytes`} was saved to ${DATA_TASK_NOTIFICATION_DETACHED_TOOL_RESULT_SAVED_TO_FILE_VAR_0.filepath}. Read that file to see it.
