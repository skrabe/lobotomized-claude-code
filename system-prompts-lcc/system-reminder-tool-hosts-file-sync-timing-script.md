<!--
name: 'System Reminder: Tool Hosts File Sync Timing Script'
description: >-
  In-script file-sync timing: a remote command's new output is taken in after
  that tool call returns, so read it on the host within the same script.
ccVersion: 2.1.261
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_FILE_SYNC_TIMING_SCRIPT_VAR_0
-->
is sent back as it finishes and taken in here once the tool call that made it has returned, before your next step, with a notice — so within one script, read a command's new output on ${SYSTEM_REMINDER_TOOL_HOSTS_FILE_SYNC_TIMING_SCRIPT_VAR_0}, not here.
