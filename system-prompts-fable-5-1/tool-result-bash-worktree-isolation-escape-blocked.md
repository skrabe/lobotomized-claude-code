<!--
name: 'Tool Result: Bash worktree isolation escape blocked'
description: >-
  Bash refusal when a worktree-isolated agent's command resolved to the shared
  checkout instead of its worktree
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_BASH_WORKTREE_ISOLATION_ESCAPE_BLOCKED_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_ISOLATION_ESCAPE_BLOCKED_VAR_1
-->
${TOOL_RESULT_BASH_WORKTREE_ISOLATION_ESCAPE_BLOCKED_VAR_0} is isolated in the worktree ${TOOL_RESULT_BASH_WORKTREE_ISOLATION_ESCAPE_BLOCKED_VAR_1}, but this command's working directory resolved to the shared checkout (${TOOL_RESULT_BASH_WORKTREE_ISOLATION_ESCAPE_BLOCKED_VAR_2}). Refusing to run it there — ${TOOL_RESULT_BASH_WORKTREE_ISOLATION_ESCAPE_BLOCKED_VAR_3} commands must run inside its worktree. Re-run the command from ${TOOL_RESULT_BASH_WORKTREE_ISOLATION_ESCAPE_BLOCKED_VAR_1}.${TOOL_RESULT_BASH_WORKTREE_ISOLATION_ESCAPE_BLOCKED_VAR_4(TOOL_RESULT_BASH_WORKTREE_ISOLATION_ESCAPE_BLOCKED_VAR_5.dir.canonical,TOOL_RESULT_BASH_WORKTREE_ISOLATION_ESCAPE_BLOCKED_VAR_5.worktree.canonical,TOOL_RESULT_BASH_WORKTREE_ISOLATION_ESCAPE_BLOCKED_VAR_1)}
