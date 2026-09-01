<!--
name: Skill Listing System-Reminder Wrapper
description: >-
  Model-facing skill_listing system-reminder wrapper injected each turn ("The
  following skills are available for use with the Skill tool:\n\n${content}");
  conditional on at least one skill being available.
ccVersion: 2.1.191
variables:
  - SYSTEM_REMINDER_SKILL_LISTING_WRAPPER_VAR_0
-->
The following skills are available for use with the Skill tool:

${SYSTEM_REMINDER_SKILL_LISTING_WRAPPER_VAR_0.content}
