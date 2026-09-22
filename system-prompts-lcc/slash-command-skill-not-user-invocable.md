<!--
name: 'Slash Command: Skill Not User Invocable'
description: >-
  Command-dispatch reply that a skill can only be invoked by Claude, so the user
  should ask Claude to run it.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_SKILL_NOT_USER_INVOCABLE_VAR_0
  - SLASH_COMMAND_SKILL_NOT_USER_INVOCABLE_VAR_1
-->
This skill can only be invoked by Claude, not directly by users. Ask Claude to use the "${SLASH_COMMAND_SKILL_NOT_USER_INVOCABLE_VAR_0(SLASH_COMMAND_SKILL_NOT_USER_INVOCABLE_VAR_1)}" skill for you.
