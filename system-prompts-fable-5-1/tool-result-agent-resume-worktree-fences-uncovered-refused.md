<!--
name: 'Tool Result: Agent Resume Permanently Refused (Fences Uncovered)'
description: >-
  Permanent AgentResumePermanentlyRefusedError for the same uncovered-fences
  condition; delivered to the model in the SendMessage resume tool result when
  the agent can never be resumed here.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_AGENT_RESUME_WORKTREE_FENCES_UNCOVERED_REFUSED_VAR_0
-->
This agent cannot be resumed: its worktree ${TOOL_RESULT_AGENT_RESUME_WORKTREE_FENCES_UNCOVERED_REFUSED_VAR_0}, and the fallback directory is not covered by the session's isolation fences.
