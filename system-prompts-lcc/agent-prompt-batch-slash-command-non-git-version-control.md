<!--
name: 'Agent Prompt: /batch non-git version control section'
description: >-
  Section added to the /batch orchestration prompt when the directory is not a
  git repo and worker worktrees come from a mod or WorktreeCreate hook. It tells
  workers to publish with the project's own VCS and report `PR: none` instead of
  a PR URL.
ccVersion: 2.1.330
variables:
  - AGENT_PROMPT_BATCH_SLASH_COMMAND_NON_GIT_VERSION_CONTROL_VAR_0
  - AGENT_PROMPT_BATCH_SLASH_COMMAND_NON_GIT_VERSION_CONTROL_VAR_1
-->

## Version control

This directory is not a git repository: worker worktrees come from a ${AGENT_PROMPT_BATCH_SLASH_COMMAND_NON_GIT_VERSION_CONTROL_VAR_0()?"mod or hook":"WorktreeCreate hook"}, so \`isolation: "worktree"\` works as above, but git and \`gh\` commands do not. ${AGENT_PROMPT_BATCH_SLASH_COMMAND_NON_GIT_VERSION_CONTROL_VAR_1} In Phase 3, a worker that reports what it published instead of a PR URL counts as done; show that report in the PR column.
