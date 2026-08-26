<!--
name: Coordinator Worker Check-In
description: >-
  Periodic task-notification reminding the coordinator model to check dispatched
  workers that are still running.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_COORDINATOR_WORKER_CHECKIN_VAR_0
  - SYSTEM_REMINDER_COORDINATOR_WORKER_CHECKIN_VAR_1
  - SYSTEM_REMINDER_COORDINATOR_WORKER_CHECKIN_VAR_2
  - SYSTEM_REMINDER_COORDINATOR_WORKER_CHECKIN_VAR_3
-->
Check-in: it has been ~${SYSTEM_REMINDER_COORDINATOR_WORKER_CHECKIN_VAR_0} minutes since you dispatched work that is still running. Check your dispatched workers. If the task is taking longer than expected, change approach and post a status saying how much longer you expect the work to take; if the work is on track, keep going — no update needed. If no response is needed, ignore this check-in.
${SYSTEM_REMINDER_COORDINATOR_WORKER_CHECKIN_VAR_1(SYSTEM_REMINDER_COORDINATOR_WORKER_CHECKIN_VAR_2,SYSTEM_REMINDER_COORDINATOR_WORKER_CHECKIN_VAR_3)}
