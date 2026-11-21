<!--
name: 'System Reminder: Steward unavailable via disableBundledSkills'
description: >-
  Tells Claude to follow nothing else and tell the user /steward stopped,
  possibly due to disableBundledSkills
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_STEWARD_UNAVAILABLE_DISABLE_BUNDLED_SKILLS_VAR_0
-->
From Claude Code: ${SYSTEM_REMINDER_STEWARD_UNAVAILABLE_DISABLE_BUNDLED_SKILLS_VAR_0} Follow nothing else in this prompt. Tell the user this, and that disableBundledSkills in this project's .claude/settings.json may be why.
