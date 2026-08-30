<!--
name: 'System Prompt: Skill disabled via skillOverrides'
description: >-
  Tells the model a skill was disabled by a skillOverrides setting and names
  removing that override as the fix.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_SKILL_DISABLED_VIA_SKILL_OVERRIDES_VAR_0
-->
Skill "${SYSTEM_PROMPT_SKILL_DISABLED_VIA_SKILL_OVERRIDES_VAR_0(SYSTEM_PROMPT_SKILL_DISABLED_VIA_SKILL_OVERRIDES_VAR_1.name,200)}" is disabled via skillOverrides. Remove the override from your settings to run it.
