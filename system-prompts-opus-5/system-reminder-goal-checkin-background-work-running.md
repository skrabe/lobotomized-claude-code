<!--
name: 'System reminder: Goal check-in background work running'
description: >-
  Injected check-in telling the model its active goal's evaluation is deferred
  while the listed background work runs, and to check on that work
ccVersion: 2.1.234
variables:
  - SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_0
  - SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_1
  - SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_2
-->
Goal check-in: «${SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_0}» is still active, and evaluation has been deferred for ${SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_1} min because background work is still running:
${SYSTEM_REMINDER_GOAL_CHECKIN_BACKGROUND_WORK_RUNNING_VAR_2.join(`
`)}
Check on their progress (e.g. read their output). If they are progressing, say so briefly and keep waiting; if they are stuck or no longer needed, fix or stop them and continue toward the goal.
