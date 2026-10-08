<!--
name: 'Data: background shell check-in notification guidance'
description: >-
  Trailing guidance of the silent-background-command check-in task notification
  telling the model to check the output file and processes, stop a hung task, or
  leave a progressing one and end its turn.
ccVersion: 2.1.294
variables:
  - DATA_TASK_NOTIFICATION_SHELL_CHECKIN_TRAILING_VAR_0
  - DATA_TASK_NOTIFICATION_SHELL_CHECKIN_TRAILING_VAR_1
  - DATA_TASK_NOTIFICATION_SHELL_CHECKIN_TRAILING_VAR_2
-->

This is a check-in, not a completion. The command may be working quietly, or it may be hung: waiting on a lock, on input, or on a process that will never exit. Find out which before you wait any longer: read its output file and look at its processes. If it is stuck, stop this task and get the work done another way. If it is making progress, or is meant to keep running (a server, a watcher), leave it and end your turn. The next check-in comes after another ${DATA_TASK_NOTIFICATION_SHELL_CHECKIN_TRAILING_VAR_0(DATA_TASK_NOTIFICATION_SHELL_CHECKIN_TRAILING_VAR_1)} of silence.${DATA_TASK_NOTIFICATION_SHELL_CHECKIN_TRAILING_VAR_2&&`
It speaks for your other background commands too, which get none of their own. Look at any that has been silent for longer than it should:${DATA_TASK_NOTIFICATION_SHELL_CHECKIN_TRAILING_VAR_2}`}
