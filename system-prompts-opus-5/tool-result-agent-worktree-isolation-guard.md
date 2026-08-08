<!--
name: 'Tool Result: Worktree isolation edit guard'
description: >-
  Reworded/merged successor of the dropped
  tool-result-agent-worktree-isolation-guard (and its session twin): the
  Edit/Write/NotebookEdit validateInput rejection telling the model to edit the
  worktree copy instead of the shared-checkout path. Id reused to preserve the
  user override.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_0
  - TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_1
  - TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_2
  - TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_3
-->
${TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_0} is isolated in the worktree ${TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_1}. Edit the worktree copy of this file instead of the shared-checkout path.${TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_2(TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_3.dir.canonical,TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_3.worktree.canonical,TOOL_RESULT_AGENT_WORKTREE_ISOLATION_GUARD_VAR_1)}
