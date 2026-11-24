<!--
name: 'System reminder: PR watch not carried over on resume'
description: >-
  Meta message telling the model a pull-request watch did not survive session
  resume (or cannot start in a background session) and must not be claimed
  active.
ccVersion: 2.1.331
variables:
  - SYSTEM_REMINDER_PR_WATCH_NOT_CARRIED_OVER_ON_RESUME_VAR_0
  - SYSTEM_REMINDER_PR_WATCH_NOT_CARRIED_OVER_ON_RESUME_VAR_1
  - SYSTEM_REMINDER_PR_WATCH_NOT_CARRIED_OVER_ON_RESUME_VAR_2
-->
From Claude Code: the watch of ${SYSTEM_REMINDER_PR_WATCH_NOT_CARRIED_OVER_ON_RESUME_VAR_0} wasn't carried over ${SYSTEM_REMINDER_PR_WATCH_NOT_CARRIED_OVER_ON_RESUME_VAR_1?"into this session, which runs in the background, where no watch can start":"when this session was resumed"}. No check-in will run, and you can't set one: only a /${SYSTEM_REMINDER_PR_WATCH_NOT_CARRIED_OVER_ON_RESUME_VAR_2} line that the user sends${SYSTEM_REMINDER_PR_WATCH_NOT_CARRIED_OVER_ON_RESUME_VAR_1?" from a claude that they run in a new terminal":""} starts a watch. The user has been told. Don't say that the watch is on.
