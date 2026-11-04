<!--
name: 'Data: Queued remote notifications REPL-script instruction'
description: >-
  REPL-mode arm of the queued-remote-notifications nudge telling the model to
  run a read script until 0 notifications remain.
ccVersion: 2.1.318
variables:
  - DATA_TASK_NOTIFICATION_QUEUED_REMOTE_NOTIFICATIONS_REPL_SCRIPT_VAR_0
-->
Before other work, run this script: \`await tools.${DATA_TASK_NOTIFICATION_QUEUED_REMOTE_NOTIFICATIONS_REPL_SCRIPT_VAR_0}({}); 'read'\`. Their text is added to the script's output, so the script needn't return anything. Repeat until the text says that 0 notifications remain queued.
