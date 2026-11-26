<!--
name: 'System Reminder: Previously invoked skills reload cut skills'
description: >-
  Lists skills whose text was cut or left out and tells Claude to reload them
  via the Skill tool before related work without repeating done work
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_PREVIOUSLY_INVOKED_SKILLS_RELOAD_CUT_SKILLS_VAR_0
  - SYSTEM_REMINDER_PREVIOUSLY_INVOKED_SKILLS_RELOAD_CUT_SKILLS_VAR_1
-->
The text of these skills was cut short or left out to save room: ${SYSTEM_REMINDER_PREVIOUSLY_INVOKED_SKILLS_RELOAD_CUT_SKILLS_VAR_0.join(", ")}. Before you do more work that one of them covers, call the ${SYSTEM_REMINDER_PREVIOUSLY_INVOKED_SKILLS_RELOAD_CUT_SKILLS_VAR_1} tool with its name, because the missing rules still apply. That is a reload, not a new run. Finished work needs no reload.
