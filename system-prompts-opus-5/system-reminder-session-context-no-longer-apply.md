<!--
name: 'System Reminder: Session context no longer applies'
description: >-
  Empty-fields branch of the session_context reminder: after a re-read, earlier
  account/project/git values no longer apply.
ccVersion: 2.1.252
variables:
  - SYSTEM_REMINDER_SESSION_CONTEXT_NO_LONGER_APPLY_VAR_0
  - SYSTEM_REMINDER_SESSION_CONTEXT_NO_LONGER_APPLY_VAR_1
-->
The session context was re-read${SYSTEM_REMINDER_SESSION_CONTEXT_NO_LONGER_APPLY_VAR_0?` ${SYSTEM_REMINDER_SESSION_CONTEXT_NO_LONGER_APPLY_VAR_1(SYSTEM_REMINDER_SESSION_CONTEXT_NO_LONGER_APPLY_VAR_0)}`:""}; the values announced earlier (account, project, git status) no longer apply.
