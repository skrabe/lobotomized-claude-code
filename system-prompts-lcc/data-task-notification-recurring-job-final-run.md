<!--
name: 'Data: Recurring job final run notice'
description: >-
  Task notification telling the model a recurring scheduled job has had its last
  run and been deleted, and to tell the user without recreating it
ccVersion: 2.1.330
variables:
  - DATA_TASK_NOTIFICATION_RECURRING_JOB_FINAL_RUN_VAR_0
  - DATA_TASK_NOTIFICATION_RECURRING_JOB_FINAL_RUN_VAR_1
  - DATA_TASK_NOTIFICATION_RECURRING_JOB_FINAL_RUN_VAR_2
  - DATA_TASK_NOTIFICATION_RECURRING_JOB_FINAL_RUN_VAR_3
-->
Recurring job ${DATA_TASK_NOTIFICATION_RECURRING_JOB_FINAL_RUN_VAR_0(DATA_TASK_NOTIFICATION_RECURRING_JOB_FINAL_RUN_VAR_1.id)} (cron ${DATA_TASK_NOTIFICATION_RECURRING_JOB_FINAL_RUN_VAR_0(DATA_TASK_NOTIFICATION_RECURRING_JOB_FINAL_RUN_VAR_1.cron)}) has had its last run, just now, and is deleted: a recurring job ends ${DATA_TASK_NOTIFICATION_RECURRING_JOB_FINAL_RUN_VAR_2(DATA_TASK_NOTIFICATION_RECURRING_JOB_FINAL_RUN_VAR_3)} after it is created. Tell the user that it has ended, and that they can ask you to create it again. Do not create it again unless they ask.
