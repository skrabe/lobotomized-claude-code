<!--
name: 'Tool Result: Worktree Create Redirected, Nothing Removed'
description: >-
  WorktreeIsolationError when containment fails because the checkout path was a
  link; nothing is removed and the model is told to inspect the pointed-to
  location.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WORKTREE_CREATE_REDIRECTED_NOTHING_REMOVED_VAR_0
-->
${TOOL_RESULT_WORKTREE_CREATE_REDIRECTED_NOTHING_REMOVED_VAR_0} Nothing was removed: the checkout was written wherever the link at that path pointed at the time, so before removing anything, check the sensitive locations it could have reached, such as .git/hooks (a hook checked out there runs on the next git command) and ~/.claude/skills. 
