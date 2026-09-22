<!--
name: 'Tool Result: Agent Resume Worktree Not Touchable'
description: >-
  Transient resume error when utimes() on the verified worktree fails with a
  non-ENOENT errno; delivered to the model in the SendMessage resume tool
  result.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_AGENT_RESUME_WORKTREE_TOUCH_FAILED_VAR_0
  - TOOL_RESULT_AGENT_RESUME_WORKTREE_TOUCH_FAILED_VAR_1
-->
Cannot resume this agent: its worktree could not be touched (${TOOL_RESULT_AGENT_RESUME_WORKTREE_TOUCH_FAILED_VAR_0(TOOL_RESULT_AGENT_RESUME_WORKTREE_TOUCH_FAILED_VAR_1??"unknown error")}). Re-run once the directory is accessible.
