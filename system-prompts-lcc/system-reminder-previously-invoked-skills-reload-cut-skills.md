<!--
name: 'System Reminder: Previously invoked skills reload cut skills'
description: >-
  Lists skills whose text was cut or left out and tells Claude to reload them
  via the Skill tool before related work without repeating done work
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_PREVIOUSLY_INVOKED_SKILLS_RELOAD_CUT_SKILLS_VAR_0
  - SYSTEM_REMINDER_PREVIOUSLY_INVOKED_SKILLS_RELOAD_CUT_SKILLS_VAR_1
-->


---

The text of these skills was cut short or left out to save room, and the missing rules still apply: ${SYSTEM_REMINDER_PREVIOUSLY_INVOKED_SKILLS_RELOAD_CUT_SKILLS_VAR_0.join(", ")}. Before your next step on work that one of them covers, call the ${SYSTEM_REMINDER_PREVIOUSLY_INVOKED_SKILLS_RELOAD_CUT_SKILLS_VAR_1} tool with its name. Treat that as a reload, not a new run: do not repeat work that is already done.
