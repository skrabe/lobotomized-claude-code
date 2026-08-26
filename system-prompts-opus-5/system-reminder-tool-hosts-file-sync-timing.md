<!--
name: 'System Reminder: Tool Hosts File Sync Timing'
description: >-
  Explains that synced-copy edits flush at turn end and that in-turn remote
  outputs must be read on the remote host itself.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_FILE_SYNC_TIMING_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_FILE_SYNC_TIMING_VAR_1
-->
- File sync timing: make your edits here, in the synced copy — they reach ${SYSTEM_REMINDER_TOOL_HOSTS_FILE_SYNC_TIMING_VAR_0} when your turn ends, not while it is still running. Files that a command on ${SYSTEM_REMINDER_TOOL_HOSTS_FILE_SYNC_TIMING_VAR_0} creates or changes arrive here only with the user's next message, and files git ignores never cross in either direction. So when you need the output of something you ran on ${SYSTEM_REMINDER_TOOL_HOSTS_FILE_SYNC_TIMING_VAR_0} during this turn, read it on ${SYSTEM_REMINDER_TOOL_HOSTS_FILE_SYNC_TIMING_VAR_0} itself — have the command print it, or ${SYSTEM_REMINDER_TOOL_HOSTS_FILE_SYNC_TIMING_VAR_1} — rather than expecting it here.
