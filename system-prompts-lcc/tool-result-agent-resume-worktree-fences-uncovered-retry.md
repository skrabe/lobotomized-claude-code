<!--
name: 'Tool Result: Agent Resume Worktree Fences Uncovered (Retry)'
description: >-
  Transient AgentResumeTransientError thrown by resumeAgentBackground when a
  parked agent's worktree is gone and the fallback dir is outside the session's
  isolation fences; its message is surfaced to the model inside the SendMessage
  tool result (`Agent "X" is stopped and could not be resumed: ${ue(T)}`).
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_AGENT_RESUME_WORKTREE_FENCES_UNCOVERED_RETRY_VAR_0
-->
Cannot resume this agent right now: its worktree ${TOOL_RESULT_AGENT_RESUME_WORKTREE_FENCES_UNCOVERED_RETRY_VAR_0}, and the fallback directory is not covered by the session's isolation fences. Re-run from a session whose fences cover the agent's directory.
