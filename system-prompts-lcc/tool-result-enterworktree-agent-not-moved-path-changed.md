<!--
name: 'Tool result: EnterWorktree agent not moved, path changed'
description: >-
  EnterWorktree error when the path no longer leads to the folder just checked;
  asks Claude to call again and tell the user if it repeats.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_ENTERWORKTREE_AGENT_NOT_MOVED_PATH_CHANGED_VAR_0
  - TOOL_RESULT_ENTERWORKTREE_AGENT_NOT_MOVED_PATH_CHANGED_VAR_1
  - TOOL_RESULT_ENTERWORKTREE_AGENT_NOT_MOVED_PATH_CHANGED_VAR_2
  - TOOL_RESULT_ENTERWORKTREE_AGENT_NOT_MOVED_PATH_CHANGED_VAR_3
-->
The agent was not moved: ${TOOL_RESULT_ENTERWORKTREE_AGENT_NOT_MOVED_PATH_CHANGED_VAR_0(TOOL_RESULT_ENTERWORKTREE_AGENT_NOT_MOVED_PATH_CHANGED_VAR_1.path)} no longer leads to the folder that was just checked. Call ${TOOL_RESULT_ENTERWORKTREE_AGENT_NOT_MOVED_PATH_CHANGED_VAR_2} again to have it checked anew, and tell the user if this happens again. The agent is still in ${TOOL_RESULT_ENTERWORKTREE_AGENT_NOT_MOVED_PATH_CHANGED_VAR_0(TOOL_RESULT_ENTERWORKTREE_AGENT_NOT_MOVED_PATH_CHANGED_VAR_3)}, so its relative paths and commands still act there, not in the worktree.
