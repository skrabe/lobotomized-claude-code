<!--
name: 'Skill: Steward Claude Code pushed and opened pull request'
description: >-
  Tells Claude that Claude Code itself pushed the branch and opened or updated
  the pull request
ccVersion: 2.1.332
variables:
  - SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_0
  - SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_1
  - SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_2
  - SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_3
  - SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_4
  - SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_5
  - SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_6
-->
Claude Code itself has just ${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_0?"committed the user's changes, ":""}pushed ${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_1.branch} and ${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_1.onto===void 0?"opened":"so added to"} pull request #${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_2.number}, and has told the user so.${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_3&&SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_4===void 0&&SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_5.onGitHub?.SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_6===!0?` Its title is a placeholder ("Add", "Remove" or "Update" and a file name), and its description says nothing of the change. Once the review is done or skipped, offer the user a title that says what changed and a description of two or three sentences, with the command that sets them: \`gh pr edit ${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_2.number} --repo ${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_1.host}/${SKILL_STEWARD_CLAUDE_CODE_PUSHED_OPENED_PR_VAR_1.repo} --title "…" --body "…"\`. Write both in plain words, with no line break, backslash, backtick, $, !, double quote, @name, link or closing keyword ("fixes #12"). That command is theirs to run.`:""}

