<!--
name: 'Tool Result: Personal hooks off when managed settings unreadable'
description: >-
  Explains hooks are off because project disableAllHooks is set and managed
  settings could not be read
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_PERSONAL_CONFIG_HOOKS_OFF_MANAGED_UNREADABLE_VAR_0
-->
the hooks in ${TOOL_RESULT_PERSONAL_CONFIG_HOOKS_OFF_MANAGED_UNREADABLE_VAR_0.join(" and ")} are turned off: the project's settings (.claude/settings.json or .claude/settings.local.json) set "disableAllHooks" and a source of your organization's managed settings could not be read, so Claude Code cannot tell whether your organization allows them
