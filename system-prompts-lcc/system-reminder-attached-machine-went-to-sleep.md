<!--
name: 'System Reminder: Attached machine went to sleep'
description: >-
  Opens the notice that an attached machine said it was going to sleep while or
  after a command was sent, followed by whether the command was withdrawn or
  left paused
ccVersion: 2.1.295
variables:
  - REMOTE_MACHINE_NAME
  - IS_WHILE_COMMAND_RUNNING
  - ASLEEP_COMMAND_STATUS_NOTE
-->
${REMOTE_MACHINE_NAME} went to sleep ${IS_WHILE_COMMAND_RUNNING?"while this command was running":"after this command was sent to it"} (it said so itself). ${ASLEEP_COMMAND_STATUS_NOTE}
