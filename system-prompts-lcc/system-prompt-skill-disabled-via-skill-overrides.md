<!--
name: 'System Prompt: Skill disabled via skillOverrides'
description: >-
  Tells the model a skill was disabled by a skillOverrides setting, names
  removing that override as the fix, and notes only an admin can remove an
  organization-set one.
ccVersion: 2.1.331
variables:
  - SYSTEM_PROMPT_SKILL_DISABLED_VIA_SKILL_OVERRIDES_VAR_0
-->
Skill "${SYSTEM_PROMPT_SKILL_DISABLED_VIA_SKILL_OVERRIDES_VAR_0}" is disabled via skillOverrides. Remove the override from your settings to run it. If your organization set it, only an admin can remove it.
