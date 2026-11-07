<!--
name: 'System Reminder: Tool host Claude Code older'
description: >-
  Tool-hosts line saying an attached machine's Claude Code is too old, so calls
  fail until it is updated
ccVersion: 2.1.319
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_HOST_OLDER_CLAUDE_CODE_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_HOST_OLDER_CLAUDE_CODE_VAR_1
-->
- ${SYSTEM_REMINDER_TOOL_HOSTS_HOST_OLDER_CLAUDE_CODE_VAR_0}: attached, but its Claude Code is older than this session works with; calls to it will fail${SYSTEM_REMINDER_TOOL_HOSTS_HOST_OLDER_CLAUDE_CODE_VAR_1} until Claude Code on it is updated (or the Claude desktop app, if that is what runs it there).
