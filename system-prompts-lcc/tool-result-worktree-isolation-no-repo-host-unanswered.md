<!--
name: 'Tool Result: Worktree isolation no-repo host unanswered'
description: >-
  Refusal when a tree holds no repository and its named checkout could not be
  confirmed or its worktree list read
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_HOST_UNANSWERED_VAR_0
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_HOST_UNANSWERED_VAR_0} as an isolation worktree: it holds no git repository and the checkout whose .claude/worktrees its path names gave no answer about it (that checkout's own repository could not be confirmed, or its worktree list could not be read). Fix that checkout first, or recreate the worktree from it.
