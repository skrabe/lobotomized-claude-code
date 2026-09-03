<!--
name: 'System Reminder: Tool Hosts Here Refreshed Copy'
description: >-
  Describes the default local host as an upload-only refreshed copy whose edits
  are not written back to the user's machine.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_HERE_REFRESHED_COPY_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_HERE_REFRESHED_COPY_VAR_1
-->
- ${SYSTEM_REMINDER_TOOL_HOSTS_HERE_REFRESHED_COPY_VAR_0()} (default): ${SYSTEM_REMINDER_TOOL_HOSTS_HERE_REFRESHED_COPY_VAR_1} — the user's current files (their saved changes arrive here before each of their messages) plus the project's toolchain. Reads, search, builds, tests and anything long-running belong here; but edits made here are NOT carried back to the user's machine — make changes the user should keep on that machine, or commit and push them here and say so.
