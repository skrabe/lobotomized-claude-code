<!--
name: 'System Reminder: Cloud worker replaced ask folder again clause'
description: >-
  Clause telling the model, after the cloud worker was replaced, to request each
  online machine's folder again once before asking the user to check it
ccVersion: 2.1.319
variables:
  - SYSTEM_REMINDER_CLOUD_WORKER_REPLACED_ASK_FOLDER_AGAIN_CLAUSE_VAR_0
  - SYSTEM_REMINDER_CLOUD_WORKER_REPLACED_ASK_FOLDER_AGAIN_CLAUSE_VAR_1
  - SYSTEM_REMINDER_CLOUD_WORKER_REPLACED_ASK_FOLDER_AGAIN_CLAUSE_VAR_2
-->
call ${SYSTEM_REMINDER_CLOUD_WORKER_REPLACED_ASK_FOLDER_AGAIN_CLAUSE_VAR_0} and, ${SYSTEM_REMINDER_CLOUD_WORKER_REPLACED_ASK_FOLDER_AGAIN_CLAUSE_VAR_1?"if that machine is":"for each of those machines that is"} listed as online, ask for its folder again with ${SYSTEM_REMINDER_CLOUD_WORKER_REPLACED_ASK_FOLDER_AGAIN_CLAUSE_VAR_2}, once (the user approves the request). If ${SYSTEM_REMINDER_CLOUD_WORKER_REPLACED_ASK_FOLDER_AGAIN_CLAUSE_VAR_1?"it":"one"} is not online, or that does not bring it back, 
