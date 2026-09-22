<!--
name: 'Tool Result: Agent Resume Worktree Not Examinable'
description: >-
  Transient resume error when stat() on the parked agent's worktree fails with
  something other than ENOENT/ENOTDIR; reaches the model through the SendMessage
  resume tool result.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_AGENT_RESUME_WORKTREE_STAT_FAILED_VAR_0
  - TOOL_RESULT_AGENT_RESUME_WORKTREE_STAT_FAILED_VAR_1
-->
Cannot resume this agent: its worktree could not be examined (${TOOL_RESULT_AGENT_RESUME_WORKTREE_STAT_FAILED_VAR_0(TOOL_RESULT_AGENT_RESUME_WORKTREE_STAT_FAILED_VAR_1??"unknown error")}). Re-run once the directory is accessible.
