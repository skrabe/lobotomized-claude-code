<!--
name: Agent worktree isolation guard
description: >-
  Edit/Write/NotebookEdit validation error returned to the model when an
  isolated agent or session edits a shared-checkout path. 2.1.224 merged the
  session variant in: the subject ("This agent" / "This session") is now slot 0
  and the worktree path is slot 1, so the old ${VAR_0.agentWorktree} property
  access no longer resolves. Fable trim: the trailing hint call is dropped.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_0
  - TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_1
  - TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_2
  - TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_3
-->
${TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_0} is isolated in the worktree ${TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_1}. Edit the worktree copy of this file instead of the shared-checkout path.
