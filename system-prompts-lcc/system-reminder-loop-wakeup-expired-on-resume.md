<!--
name: 'System Reminder: Loop wakeup expired on resume'
description: >-
  Explains that the previous process's overdue wakeup will not fire and asks the
  model to reschedule only if the loop remains wanted.
ccVersion: 2.1.295
variables:
  - SYSTEM_REMINDER_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_0
  - SYSTEM_REMINDER_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_1
-->

<${SYSTEM_REMINDER_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_0}>The wakeup scheduled by the ${SYSTEM_REMINDER_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_1} call this notification names was still pending when this session's process ended, and its fire time passed before a new process took the session over. It will not fire. A ${SYSTEM_REMINDER_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_1} call made since the new process started is not affected. Otherwise nothing wakes this session for the loop: call ${SYSTEM_REMINDER_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_1} again only if the loop is still wanted, and when the conversation does not make that clear, ask the user first.</${SYSTEM_REMINDER_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_0}>
