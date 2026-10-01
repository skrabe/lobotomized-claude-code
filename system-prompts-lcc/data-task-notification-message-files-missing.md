<!--
name: 'Task notification: message files missing'
description: >-
  Queued task-notification (wrapped in <message-files-missing>) telling the
  model which file paths named in a user message were not written because their
  attachments could not be fetched.
ccVersion: 2.1.286
variables:
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_0
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_1
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_2
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_3
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_4
-->

<${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_0}>
${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_1.length} of the ${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_2} file(s) attached to a user message could not be fetched or saved, so these paths, which the message names, were not written: ${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_1.map((DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_3)=>DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_4(DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_3.slice(1))).join(", ")}
</${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_0}>
