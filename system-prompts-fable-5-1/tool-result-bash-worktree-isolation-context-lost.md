<!--
name: 'Tool Result: Bash worktree isolation context lost'
description: >-
  Bash refusal when an agent's worktree isolation context was lost so the
  command would run in the parent directory
ccVersion: 2.1.204
variables:
  - TOOL_RESULT_BASH_WORKTREE_ISOLATION_CONTEXT_LOST_VAR_0
-->
The working-directory isolation context for this agent was lost, so this command would run in the parent session's directory instead of this agent's worktree (${TOOL_RESULT_BASH_WORKTREE_ISOLATION_CONTEXT_LOST_VAR_0}). Refusing to run it. Retry the command; if this keeps failing, report that worktree isolation was lost.
