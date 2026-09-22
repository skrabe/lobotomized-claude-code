<!--
name: 'Tool Result: Agent Resume Worktree Root Refused'
description: >-
  Permanent resume refusal when the worktree-root containment check rejects the
  parked agent's worktree; surfaced to the model via the SendMessage resume tool
  result.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_AGENT_RESUME_WORKTREE_ROOT_REFUSED_VAR_0
-->
This agent cannot be resumed: its worktree was refused (${TOOL_RESULT_AGENT_RESUME_WORKTREE_ROOT_REFUSED_VAR_0.reason}). ${TOOL_RESULT_AGENT_RESUME_WORKTREE_ROOT_REFUSED_VAR_0.message}
