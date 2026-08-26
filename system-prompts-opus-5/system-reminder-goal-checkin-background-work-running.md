<!--
name: 'System Reminder: Goal Check-In Background Work Running'
description: >-
  Reminds the model a goal check-in was deferred because background work is
  still running.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_0
  - SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_1
  - SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_2
  - SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_3
-->
${SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_0}${SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_1}» is still active, and evaluation has been deferred for ${SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_2} min because background work is still running:
${SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_3.join(`
`)}
Check on their progress (e.g. read their output). If they are progressing, say so briefly and keep waiting; if they are stuck or no longer needed, fix or stop them and continue toward the goal.
