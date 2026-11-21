<!--
name: 'Tool result: cron other one-shot tasks pending'
description: >-
  CronCreate result appendix listing other pending session-only one-shot tasks
  and when to cancel them.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_CRON_OTHER_ONESHOT_TASKS_PENDING_VAR_0
  - TOOL_RESULT_CRON_OTHER_ONESHOT_TASKS_PENDING_VAR_1
  - TOOL_RESULT_CRON_OTHER_ONESHOT_TASKS_PENDING_VAR_2
-->

Other session-only one-shot tasks that have yet to fire:
${TOOL_RESULT_CRON_OTHER_ONESHOT_TASKS_PENDING_VAR_0.otherOneShots.map((TOOL_RESULT_CRON_OTHER_ONESHOT_TASKS_PENDING_VAR_1)=>`${TOOL_RESULT_CRON_OTHER_ONESHOT_TASKS_PENDING_VAR_1.id} — ${TOOL_RESULT_CRON_OTHER_ONESHOT_TASKS_PENDING_VAR_1.humanSchedule}: ${TOOL_RESULT_CRON_OTHER_ONESHOT_TASKS_PENDING_VAR_1.prompt}`).join(`
`)}
If the new task or a newer instruction makes one of these out of date, cancel it with ${TOOL_RESULT_CRON_OTHER_ONESHOT_TASKS_PENDING_VAR_2}. Keep reminders that a person asked for, and checks on other work.
