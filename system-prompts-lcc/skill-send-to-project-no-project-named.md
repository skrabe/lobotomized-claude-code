<!--
name: 'Skill: /send-to-project no project with that name'
description: >-
  Says none of the user's personal projects has the given name, noting
  shared/paused/archived ones and quote-led messages cannot be named
ccVersion: 2.1.314
variables:
  - SKILL_SEND_TO_PROJECT_NO_PROJECT_NAMED_VAR_0
  - SKILL_SEND_TO_PROJECT_NO_PROJECT_NAMED_VAR_1
  - SKILL_SEND_TO_PROJECT_NO_PROJECT_NAMED_VAR_2
  - SKILL_SEND_TO_PROJECT_NO_PROJECT_NAMED_VAR_3
-->
None of your ${SKILL_SEND_TO_PROJECT_NO_PROJECT_NAMED_VAR_0?`${SKILL_SEND_TO_PROJECT_NO_PROJECT_NAMED_VAR_1} most recently active `:""}personal projects is named “${SKILL_SEND_TO_PROJECT_NO_PROJECT_NAMED_VAR_2(SKILL_SEND_TO_PROJECT_NO_PROJECT_NAMED_VAR_3.trim(),80)}”. A project that is shared, paused or archived can’t be named here, and a message can’t open with a double quote. ${"Run /send-to-project alone to pick the project."}
