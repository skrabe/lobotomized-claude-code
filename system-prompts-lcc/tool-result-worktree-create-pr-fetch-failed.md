<!--
name: 'Tool Result: Worktree Create Pr Fetch Failed'
description: >-
  Error text from worktree create when fetching PR/MR head from origin fails,
  surfaced as the tool result.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_WORKTREE_CREATE_PR_FETCH_FAILED_VAR_0
  - TOOL_RESULT_WORKTREE_CREATE_PR_FETCH_FAILED_VAR_1
  - TOOL_RESULT_WORKTREE_CREATE_PR_FETCH_FAILED_VAR_2
  - TOOL_RESULT_WORKTREE_CREATE_PR_FETCH_FAILED_VAR_3
-->
Failed to fetch PR/MR #${TOOL_RESULT_WORKTREE_CREATE_PR_FETCH_FAILED_VAR_0.prNumber}: ${TOOL_RESULT_WORKTREE_CREATE_PR_FETCH_FAILED_VAR_1(TOOL_RESULT_WORKTREE_CREATE_PR_FETCH_FAILED_VAR_2(TOOL_RESULT_WORKTREE_CREATE_PR_FETCH_FAILED_VAR_3.trim()))||'it may not exist, the fetch may have timed out, or the repository may not have a remote named "origin"'}
