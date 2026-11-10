<!--
name: 'System Reminder: Low disk space'
description: >-
  Resource watchdog reminder that only a little disk space is free on the
  filesystem holding the working directory, with what to do if room is needed
ccVersion: 2.1.322
variables:
  - SYSTEM_REMINDER_LOW_DISK_SPACE_VAR_0
  - SYSTEM_REMINDER_LOW_DISK_SPACE_VAR_1
  - SYSTEM_REMINDER_LOW_DISK_SPACE_VAR_2
-->
${SYSTEM_REMINDER_LOW_DISK_SPACE_VAR_0}${SYSTEM_REMINDER_LOW_DISK_SPACE_VAR_1(SYSTEM_REMINDER_LOW_DISK_SPACE_VAR_2)} free on the filesystem holding the working directory. If you need room, delete temporary files that you made. Ask the user before you delete any other file. If that does not free enough, tell the user.
