<!--
name: 'Agent Prompt: /batch not in a git repository'
description: >-
  Explains /batch cannot create worktrees because the directory is not a git
  repository
ccVersion: 2.1.326
variables:
  - AGENT_PROMPT_BATCH_SLASH_COMMAND_NOT_GIT_REPOSITORY_VAR_0
-->
The \`/batch\` command runs each agent in its own isolated worktree, and none can be created here: this directory is not in a git repository. ${AGENT_PROMPT_BATCH_SLASH_COMMAND_NOT_GIT_REPOSITORY_VAR_0}
