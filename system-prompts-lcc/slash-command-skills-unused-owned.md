<!--
name: 'Slash command: skills unused owned'
description: >-
  Skills usage report warning that the user's own skills were loaded but never
  used, with how to disable them.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_SKILLS_UNUSED_OWNED_VAR_0
  - SLASH_COMMAND_SKILLS_UNUSED_OWNED_VAR_1
-->
${SLASH_COMMAND_SKILLS_UNUSED_OWNED_VAR_0.length} ${SLASH_COMMAND_SKILLS_UNUSED_OWNED_VAR_1(SLASH_COMMAND_SKILLS_UNUSED_OWNED_VAR_0.length,"skill")} loaded but never used. Each one adds to the system prompt every turn. Disable in /skills, or remove from .claude/skills.
