<!--
name: 'System Reminder: Runner left repository out line'
description: >-
  Per-repository bullet naming a repository (or another source of the same name)
  the runner left out at this start and why, joined into the
  left-out-repositories reminder
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_RUNNER_LEFT_REPOSITORY_OUT_LINE_VAR_0
  - SYSTEM_REMINDER_RUNNER_LEFT_REPOSITORY_OUT_LINE_VAR_1
  - SYSTEM_REMINDER_RUNNER_LEFT_REPOSITORY_OUT_LINE_VAR_2
  - SYSTEM_REMINDER_RUNNER_LEFT_REPOSITORY_OUT_LINE_VAR_3
-->
- At this start ${SYSTEM_REMINDER_RUNNER_LEFT_REPOSITORY_OUT_LINE_VAR_0(SYSTEM_REMINDER_RUNNER_LEFT_REPOSITORY_OUT_LINE_VAR_1)?`${SYSTEM_REMINDER_RUNNER_LEFT_REPOSITORY_OUT_LINE_VAR_2} \`${SYSTEM_REMINDER_RUNNER_LEFT_REPOSITORY_OUT_LINE_VAR_1}\``:"one of this session's repositories"} was left out: ${SYSTEM_REMINDER_RUNNER_LEFT_REPOSITORY_OUT_LINE_VAR_3}.
