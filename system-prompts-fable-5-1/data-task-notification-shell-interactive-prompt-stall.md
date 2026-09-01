<!--
name: 'Task Notification: Background Shell Waiting On Interactive Input'
description: >-
  Trailing text of the stalled-background-shell task notification injected into
  the agent's context, showing the last output and instructing it to stop and
  re-run with piped input or a non-interactive flag.
ccVersion: 2.1.218
variables:
  - DATA_TASK_NOTIFICATION_SHELL_INTERACTIVE_PROMPT_STALL_VAR_0
-->

Last output:
${DATA_TASK_NOTIFICATION_SHELL_INTERACTIVE_PROMPT_STALL_VAR_0.trimEnd()}

The command is likely blocked on an interactive prompt. Stop this task and re-run with piped input (e.g., \`echo y | command\`) or a non-interactive flag if one exists.
