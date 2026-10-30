<!--
name: 'Data: task notification message files missing'
description: >-
  Task-notification line listing files attached to a user message that could not
  be fetched or saved, with the affected paths
ccVersion: 2.1.314
variables:
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_0
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_1
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_2
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_3
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_4
-->
${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_0.length} of the ${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_1} file(s) attached to a user message could not be fetched or saved${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_2?" again, so these paths, which the message names, may be missing":", so these paths, which the message names, were not written"}: ${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_0.map((DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_3)=>DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_4(DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_VAR_3.slice(1))).join(", ")}
