<!--
name: 'Tool Result: Worktree-isolated git redirect blocked'
description: >-
  Bash-tool refusal returned to the model when a worktree-isolated agent's
  command would redirect git into the shared checkout.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_1
-->
${TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_0} is isolated in the worktree ${TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_1}, but this command ${TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_2}. Refusing to run it — ${TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_3} git operations must target its own worktree. Run the equivalent from ${TOOL_RESULT_WORKTREE_ISOLATED_GIT_REDIRECT_BLOCKED_VAR_1} without the redirect.
