<!--
name: 'Data: task notification code-mode send-message note (multiple agents)'
description: >-
  Suffix on a multi-agent task notification in code mode telling the model to
  message one of the listed agents via the send-message function from a script
  using its id.
ccVersion: 2.1.318
variables:
  - DATA_TASK_NOTIFICATION_CODE_MODE_SEND_MESSAGE_NOTE_MULTIPLE_VAR_0
-->
 To message one of them, call await ${DATA_TASK_NOTIFICATION_CODE_MODE_SEND_MESSAGE_NOTE_MULTIPLE_VAR_0}({to: "ID", message: "..."}) from a script, where ID is that agent's id from the list above. The previous session's contexts handles no longer work, so use the ids.
