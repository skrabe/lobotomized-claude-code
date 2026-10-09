<!--
name: 'System Reminder: Attached machine asleep command withdrawn'
description: >-
  Says the session stopped waiting on a sleeping attached machine and withdrew
  the command, which will be stopped when the machine wakes, may have partly
  run, and must not be repeated without checking
ccVersion: 2.1.295
variables:
  - REMOTE_MACHINE_NAME
-->
This session has stopped waiting for it and withdrew its request: the command will be stopped when ${REMOTE_MACHINE_NAME} wakes, and may have partly run. Do not repeat it without checking.
