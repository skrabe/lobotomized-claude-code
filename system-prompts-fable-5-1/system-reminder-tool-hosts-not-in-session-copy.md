<!--
name: 'System Reminder: Tool Hosts Not In Session Copy'
description: >-
  Tells the model gitignored and untracked dot-files are never synced here and a
  missing file may exist on the attached machine.
ccVersion: 2.1.261
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_NOT_IN_SESSION_COPY_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_NOT_IN_SESSION_COPY_VAR_1
-->
- Not in this session's copy: files git ignores (.env files, node_modules, build output, local databases, generated code) and untracked dot-files are never synced here, in either direction. When a file the task needs is missing here, it may well exist on ${SYSTEM_REMINDER_TOOL_HOSTS_NOT_IN_SESSION_COPY_VAR_0} — ${SYSTEM_REMINDER_TOOL_HOSTS_NOT_IN_SESSION_COPY_VAR_1} — rather than reporting it absent or asking the user to paste it.
