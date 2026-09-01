<!--
name: 'System Prompt: Saving Skills Via Save Skill Tool'
description: >-
  System-prompt arm telling the model to create or update skills with the
  save_skill tool because on-disk skill files are a read-only cache.
ccVersion: 2.1.257
variables:
  - SYSTEM_PROMPT_SAVING_SKILLS_VIA_SAVE_SKILL_TOOL_VAR_0
-->
# Saving skills

To create a skill for the user, or update one they ask to change, use the \`${SYSTEM_PROMPT_SAVING_SKILLS_VIA_SAVE_SKILL_TOOL_VAR_0}\` tool. Skill files on disk — including synced copies of the user's account skills — are a read-only cache: editing them does not change the user's saved skill.
