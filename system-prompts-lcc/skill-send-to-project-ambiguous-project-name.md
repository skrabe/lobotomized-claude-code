<!--
name: 'Skill: /send-to-project ambiguous project name'
description: Says more than one of the user's Claude Projects has the given name
ccVersion: 2.1.314
variables:
  - SKILL_SEND_TO_PROJECT_AMBIGUOUS_PROJECT_NAME_VAR_0
  - SKILL_SEND_TO_PROJECT_AMBIGUOUS_PROJECT_NAME_VAR_1
-->
More than one of your Claude Projects is named “${SKILL_SEND_TO_PROJECT_AMBIGUOUS_PROJECT_NAME_VAR_0(SKILL_SEND_TO_PROJECT_AMBIGUOUS_PROJECT_NAME_VAR_1.name,80)}”. ${"Run /send-to-project alone to pick the project."}
