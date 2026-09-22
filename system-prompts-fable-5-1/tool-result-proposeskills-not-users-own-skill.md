<!--
name: Propose Skills Not User's Own Skill
description: >-
  Tells the model a built-in or plugin skill cannot be updated by the review
  card and to propose a new skill instead.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_PROPOSESKILLS_NOT_USERS_OWN_SKILL_VAR_0
  - TOOL_RESULT_PROPOSESKILLS_NOT_USERS_OWN_SKILL_VAR_1
  - TOOL_RESULT_PROPOSESKILLS_NOT_USERS_OWN_SKILL_VAR_2
  - TOOL_RESULT_PROPOSESKILLS_NOT_USERS_OWN_SKILL_VAR_3
  - TOOL_RESULT_PROPOSESKILLS_NOT_USERS_OWN_SKILL_VAR_4
-->
${TOOL_RESULT_PROPOSESKILLS_NOT_USERS_OWN_SKILL_VAR_0.target}${TOOL_RESULT_PROPOSESKILLS_NOT_USERS_OWN_SKILL_VAR_1} is ${TOOL_RESULT_PROPOSESKILLS_NOT_USERS_OWN_SKILL_VAR_2}, not one of the user's own skills, so the review card cannot update it. To customize it for the user, propose kind "new" under a name of its own — not ${TOOL_RESULT_PROPOSESKILLS_NOT_USERS_OWN_SKILL_VAR_3} — with a description that says when to use it instead of ${TOOL_RESULT_PROPOSESKILLS_NOT_USERS_OWN_SKILL_VAR_4.name}.
