<!--
name: 'Skill: Steward Claude Code pushed and opened pull request'
description: >-
  Tells Claude that Claude Code itself pushed the branch and opened or updated
  the pull request
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_0
  - SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_1
  - SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_2
-->
Claude Code itself has just ${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_0?"committed the user's changes, ":""}pushed ${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_1.branch} and ${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_1.onto===void 0?"opened":"so added to"} pull request #${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_2.number}, and has told the user so.

