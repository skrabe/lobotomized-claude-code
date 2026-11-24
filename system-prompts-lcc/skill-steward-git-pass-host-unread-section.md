<!--
name: 'Steward: git pass, host not read section'
description: >-
  Section of the git pass prompt saying Claude Code can't read the host's web
  API now, so git alone watches; tell the user.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_GIT_PASS_HOST_UNREAD_SECTION_VAR_0
  - SKILL_STEWARD_GIT_PASS_HOST_UNREAD_SECTION_VAR_1
  - SKILL_STEWARD_GIT_PASS_HOST_UNREAD_SECTION_VAR_2
-->
## What ${SKILL_STEWARD_GIT_PASS_HOST_UNREAD_SECTION_VAR_0} says

Claude Code reads ${SKILL_STEWARD_GIT_PASS_HOST_UNREAD_SECTION_VAR_0}'s web API itself, but ${SKILL_STEWARD_GIT_PASS_HOST_UNREAD_SECTION_VAR_1.checks.why==="new_each_time"?`${SKILL_STEWARD_GIT_PASS_HOST_UNREAD_SECTION_VAR_2(SKILL_STEWARD_GIT_PASS_HOST_UNREAD_SECTION_VAR_1.checks.why)}. For the rest of this watch git alone watches`:`for now ${SKILL_STEWARD_GIT_PASS_HOST_UNREAD_SECTION_VAR_2(SKILL_STEWARD_GIT_PASS_HOST_UNREAD_SECTION_VAR_1.request.why??SKILL_STEWARD_GIT_PASS_HOST_UNREAD_SECTION_VAR_1.checks.why??"no_answer")}. It goes on trying, and git alone watches meanwhile`}: you see no checks and no comments. Tell the user so in one line.

