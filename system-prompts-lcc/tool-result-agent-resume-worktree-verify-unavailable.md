<!--
name: 'Tool Result: Agent Resume Worktree Unverifiable'
description: >-
  Transient resume error when the worktree containment check is 'unverifiable'
  this attempt; the model reads it in the SendMessage resume tool result and can
  retry.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_AGENT_RESUME_WORKTREE_VERIFY_UNAVAILABLE_VAR_0
-->
Cannot resume this agent right now: its worktree could not be verified (${TOOL_RESULT_AGENT_RESUME_WORKTREE_VERIFY_UNAVAILABLE_VAR_0.reason}). Re-run once git can answer.
