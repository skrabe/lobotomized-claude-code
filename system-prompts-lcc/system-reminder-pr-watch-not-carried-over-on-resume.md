<!--
name: 'System reminder: PR watch not carried over on resume'
description: >-
  Meta message telling the model a pull-request watch did not survive session
  resume and must not be claimed active.
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_PR_WATCH_NOT_CARRIED_OVER_ON_RESUME_VAR_0
  - SYSTEM_REMINDER_PR_WATCH_NOT_CARRIED_OVER_ON_RESUME_VAR_1
-->
From Claude Code: the watch of pull request #${SYSTEM_REMINDER_PR_WATCH_NOT_CARRIED_OVER_ON_RESUME_VAR_0.pr} wasn't carried over when this session was resumed. No check-in will run, and you can't set one: only a /${SYSTEM_REMINDER_PR_WATCH_NOT_CARRIED_OVER_ON_RESUME_VAR_1} line that the user sends starts a watch. The user has been told. Don't say that the watch is on.
