<!--
name: 'System Reminder: Tool host needs newer session'
description: >-
  Tool-hosts line saying an attached machine's Claude Code needs a newer session
  build, so calls fail until the cloud environment is updated
ccVersion: 2.1.319
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_HOST_NEWER_CLAUDE_CODE_REQUIRED_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_HOST_NEWER_CLAUDE_CODE_REQUIRED_VAR_1
-->
- ${SYSTEM_REMINDER_TOOL_HOSTS_HOST_NEWER_CLAUDE_CODE_REQUIRED_VAR_0}: attached, but its Claude Code works only with a newer Claude Code than this session runs; calls to it will fail${SYSTEM_REMINDER_TOOL_HOSTS_HOST_NEWER_CLAUDE_CODE_REQUIRED_VAR_1} until this session has a newer cloud environment; nothing needs changing on the machine.
