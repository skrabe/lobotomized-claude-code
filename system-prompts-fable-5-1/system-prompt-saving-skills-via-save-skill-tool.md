<!--
name: 'System Prompt: Saving skills via save_skill tool'
description: >-
  In-session skill-editing guidance: on-disk skill files are a read-only cache,
  so create/update skills through the save_skill tool.
ccVersion: 2.1.218
variables:
  - SYSTEM_PROMPT_SAVING_SKILLS_VIA_SAVE_SKILL_TOOL_VAR_0
-->
# Saving skills

Skill files on disk in this session — including synced copies of the user's account skills — are a read-only cache: editing them does not change the user's saved skill. To create a skill, or update one the user asks to change, use the \`${SYSTEM_PROMPT_SAVING_SKILLS_VIA_SAVE_SKILL_TOOL_VAR_0}\` tool.
