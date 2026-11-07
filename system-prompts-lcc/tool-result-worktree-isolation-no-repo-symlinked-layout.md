<!--
name: 'Tool Result: Worktree isolation no-repo symlinked layout'
description: >-
  Refusal when a tree without its own repository sits under a symlinked or
  unresolved checkout path
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SYMLINKED_LAYOUT_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SYMLINKED_LAYOUT_VAR_1
  - TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SYMLINKED_LAYOUT_VAR_2
  - TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SYMLINKED_LAYOUT_VAR_3
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SYMLINKED_LAYOUT_VAR_0} as an isolation worktree: ${TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SYMLINKED_LAYOUT_VAR_1(TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SYMLINKED_LAYOUT_VAR_2(TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SYMLINKED_LAYOUT_VAR_0))} or the directory above it is a symbolic link or junction (or the checkout's own path could not be resolved), so the tree is not really inside the checkout its path names, and it holds no git repository of its own. Claude Code never creates such a link: open the tree by its real path, or treat it as tampered with and recreate the worktree from ${TOOL_RESULT_WORKTREE_ISOLATION_NO_REPO_SYMLINKED_LAYOUT_VAR_3}.
