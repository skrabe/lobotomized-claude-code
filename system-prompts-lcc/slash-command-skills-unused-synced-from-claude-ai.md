<!--
name: 'Slash command: skills unused synced from claude.ai'
description: >-
  Skills usage report warning that synced claude.ai skills were loaded but never
  used, with how to disable them.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_SKILLS_UNUSED_SYNCED_FROM_CLAUDE_AI_VAR_0
  - SLASH_COMMAND_SKILLS_UNUSED_SYNCED_FROM_CLAUDE_AI_VAR_1
-->
${SLASH_COMMAND_SKILLS_UNUSED_SYNCED_FROM_CLAUDE_AI_VAR_0.length} ${SLASH_COMMAND_SKILLS_UNUSED_SYNCED_FROM_CLAUDE_AI_VAR_1(SLASH_COMMAND_SKILLS_UNUSED_SYNCED_FROM_CLAUDE_AI_VAR_0.length,"skill")} synced from claude.ai loaded but never used. Each one adds to the system prompt every turn. Disable in /skills, or turn ${SLASH_COMMAND_SKILLS_UNUSED_SYNCED_FROM_CLAUDE_AI_VAR_0.length===1?"it":"them"} off on claude.ai — a deleted synced copy is re-downloaded on the next sync.
