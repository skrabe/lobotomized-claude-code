<!--
name: 'Tool Result: Agent worktree hook path not directory'
description: Reports a WorktreeCreate or mod hook returned a path that is not a directory
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_AGENT_WORKTREE_HOOK_PATH_NOT_DIRECTORY_VAR_0
  - TOOL_RESULT_AGENT_WORKTREE_HOOK_PATH_NOT_DIRECTORY_VAR_1
-->
${TOOL_RESULT_AGENT_WORKTREE_HOOK_PATH_NOT_DIRECTORY_VAR_0==="hook"?"WorktreeCreate":`The ${TOOL_RESULT_AGENT_WORKTREE_HOOK_PATH_NOT_DIRECTORY_VAR_0}`} hook returned a path that is not a directory: ${TOOL_RESULT_AGENT_WORKTREE_HOOK_PATH_NOT_DIRECTORY_VAR_1}. The hook must create the directory before ${TOOL_RESULT_AGENT_WORKTREE_HOOK_PATH_NOT_DIRECTORY_VAR_0==="hook"?"echoing":"answering"} its path.
