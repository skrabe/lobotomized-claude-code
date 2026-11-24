<!--
name: 'Skill: Steward Claude Code acted for user'
description: >-
  Tells the model that Claude Code itself already acted for the user
  (pushed/opened the PR) and that the reply's opening words say so.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_CLAUDE_CODE_ACTED_FOR_USER_VAR_0
  - SKILL_STEWARD_CLAUDE_CODE_ACTED_FOR_USER_VAR_1
-->
Claude Code itself has just acted for the user. The words below that open your reply say what it did, and name the pull request.${SKILL_STEWARD_CLAUDE_CODE_ACTED_FOR_USER_VAR_0.includes(SKILL_STEWARD_CLAUDE_CODE_ACTED_FOR_USER_VAR_1)?SKILL_STEWARD_CLAUDE_CODE_ACTED_FOR_USER_VAR_0.slice(SKILL_STEWARD_CLAUDE_CODE_ACTED_FOR_USER_VAR_0.indexOf(SKILL_STEWARD_CLAUDE_CODE_ACTED_FOR_USER_VAR_1)+SKILL_STEWARD_CLAUDE_CODE_ACTED_FOR_USER_VAR_1.length):`

`}
