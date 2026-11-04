<!--
name: 'Data: task notification code-mode send-message note (single agent)'
description: >-
  Suffix on a background-agent task notification in code mode telling the model
  to message the agent via the send-message function from a script using its
  task id, since old contexts handles no longer work.
ccVersion: 2.1.318
variables:
  - DATA_TASK_NOTIFICATION_CODE_MODE_SEND_MESSAGE_NOTE_SINGLE_VAR_0
-->
 To message it, call await ${DATA_TASK_NOTIFICATION_CODE_MODE_SEND_MESSAGE_NOTE_SINGLE_VAR_0}({to: "ID", message: "..."}) from a script, where ID is the task id above. The previous session's contexts handles no longer work, so use the id.
