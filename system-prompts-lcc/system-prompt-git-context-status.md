<!--
name: Git context — status block
description: Git context includes configured Git user and worktree status.
ccVersion: 2.1.322
variables:
  - SYSTEM_PROMPT_GIT_CONTEXT_STATUS_VAR_0
  - SYSTEM_PROMPT_GIT_CONTEXT_STATUS_VAR_1
-->
Status:
${SYSTEM_PROMPT_GIT_CONTEXT_STATUS_VAR_0||"(clean)"}${SYSTEM_PROMPT_GIT_CONTEXT_STATUS_VAR_1}
