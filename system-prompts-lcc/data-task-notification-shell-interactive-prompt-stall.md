<!--
name: Task Notification Shell Interactive Prompt Stall
description: >-
  Task-notification trailing text telling the model a background shell looks
  blocked on an interactive prompt.
ccVersion: 2.1.261
variables:
  - DATA_TASK_NOTIFICATION_SHELL_INTERACTIVE_PROMPT_STALL_VAR_0
  - DATA_TASK_NOTIFICATION_SHELL_INTERACTIVE_PROMPT_STALL_VAR_1
-->

Last output:
${DATA_TASK_NOTIFICATION_SHELL_INTERACTIVE_PROMPT_STALL_VAR_0(DATA_TASK_NOTIFICATION_SHELL_INTERACTIVE_PROMPT_STALL_VAR_1).trimEnd()}

The command is likely blocked on an interactive prompt. Stop this task and re-run with piped input (e.g., \`echo y | command\`) or a non-interactive flag if one exists.
