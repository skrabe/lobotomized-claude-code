<!--
name: 'System Reminder: Cloud sandbox sustained CPU limit stop'
description: >-
  Reports shell work stopped after sustained near-full CPU use and requires
  agreement on a lower-CPU approach before restarting heavy work
ccVersion: 2.1.314
variables:
  - FORMAT_DURATION_FN
  - SUSTAINED_FULL_CPU_DURATION_MS
  - FULL_CPU_STOP_LIMIT_MS
  - STOPPED_COMMAND_DESCRIPTIONS
-->
This cloud sandbox used 90% or more of all its CPUs for ${FORMAT_DURATION_FN(SUSTAINED_FULL_CPU_DURATION_MS)}, almost without a break. The limit is ${FORMAT_DURATION_FN(FULL_CPU_STOP_LIMIT_MS)}. At the limit, Claude Code stops the shell commands of this session and the processes that they started, also those that used little CPU. The commands themselves did not fail. The files are kept. Commands that use little CPU, such as a dev server, can start again. Work that fills the CPUs again will be stopped again, so do not start it again in the same form. Tell the user what was stopped and why. If the heavy work is still necessary, first agree with the user on a form that uses less CPU, for example a smaller job or fewer parallel workers.${STOPPED_COMMAND_DESCRIPTIONS&&` Stopped commands: ${STOPPED_COMMAND_DESCRIPTIONS}.`}
