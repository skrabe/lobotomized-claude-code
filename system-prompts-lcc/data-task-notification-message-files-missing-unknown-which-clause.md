<!--
name: 'Data: task notification files missing, unknown which'
description: >-
  Task-notification line saying some files attached to an earlier user message
  may be missing from the uploads folder and to ask the user to reattach any
  named file not found
ccVersion: 2.1.314
variables:
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_UNKNOWN_WHICH_CLAUSE_VAR_0
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_UNKNOWN_WHICH_CLAUSE_VAR_1
  - DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_UNKNOWN_WHICH_CLAUSE_VAR_2
-->
${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_UNKNOWN_WHICH_CLAUSE_VAR_0.length>0?`${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_UNKNOWN_WHICH_CLAUSE_VAR_1} more of them may be missing too`:`${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_UNKNOWN_WHICH_CLAUSE_VAR_1} of the ${DATA_TASK_NOTIFICATION_MESSAGE_FILES_MISSING_UNKNOWN_WHICH_CLAUSE_VAR_2} file(s) attached to an earlier user message may be missing from the uploads folder`}, and it is not known which. If a file that the conversation names in the uploads folder is not found, ask the user to attach it again.
