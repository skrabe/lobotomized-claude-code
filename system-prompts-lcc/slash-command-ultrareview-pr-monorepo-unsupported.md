<!--
name: 'Slash Command: Ultrareview — PR Review Unsupported in This Repository'
description: >-
  Ultrareview precondition error when PR review is blocked for this (monorepo)
  repository, suggesting /code-review <PR> for a local review instead.
ccVersion: 2.1.282
variables:
  - SLASH_COMMAND_ULTRAREVIEW_PR_MONOREPO_UNSUPPORTED_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_PR_MONOREPO_UNSUPPORTED_VAR_1
-->
${SLASH_COMMAND_ULTRAREVIEW_PR_MONOREPO_UNSUPPORTED_VAR_0} doesn't support pull requests in this repository. Run /code-review ${SLASH_COMMAND_ULTRAREVIEW_PR_MONOREPO_UNSUPPORTED_VAR_1}${SLASH_COMMAND_ULTRAREVIEW_PR_MONOREPO_UNSUPPORTED_VAR_0.startsWith("/")?"":" in Claude Code"} for a local review instead.
