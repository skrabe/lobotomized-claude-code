<!--
name: 'Tool Result: Worktree Create Redirected, Nothing Removed'
description: >-
  WorktreeIsolationError when containment fails because the checkout path was a
  link; nothing is removed and the model is told to inspect the pointed-to
  location.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_WORKTREE_CREATE_REDIRECTED_NOTHING_REMOVED_VAR_0
  - TOOL_RESULT_WORKTREE_CREATE_REDIRECTED_NOTHING_REMOVED_VAR_1
-->
${TOOL_RESULT_WORKTREE_CREATE_REDIRECTED_NOTHING_REMOVED_VAR_0} Nothing was removed: the checkout was written wherever the link at that path pointed at the time, so inspect that location (and any sensitive one it could reach, such as .git/hooks, where a checked-out hook runs on the next git command) before removing anything. The worktree registration for ${TOOL_RESULT_WORKTREE_CREATE_REDIRECTED_NOTHING_REMOVED_VAR_1} was left in place; \`git worktree list\` shows what git lists on it.
