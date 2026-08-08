<!--
name: 'Tool Result: Worktree-isolated git redirect blocked'
description: >-
  Bash tool result emitted when a worktree-isolated session/agent runs a git
  command that redirects out of its worktree; reworded from the 2.1.221 id
  (noun/possessive now parameterised for sessions vs agents).
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_1
  - TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_2
  - TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_3
-->
${TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_0} is isolated in the worktree ${TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_1}, but this command ${TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_2}. Refusing to run it — ${TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_3} git operations must target its own worktree. Run the equivalent from ${TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_1} without the redirect.
