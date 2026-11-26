<!--
name: 'Slash Command: /ultrareview — Committed Work Counts As Base'
description: >-
  Explanation in the empty-diff error that everything already committed on the
  base branch counts as the base, so only uncommitted edits would be reviewed.
ccVersion: 2.1.332
variables:
  - SLASH_COMMAND_ULTRAREVIEW_EMPTY_DIFF_BASE_BRANCH_COMMITS_COUNT_AS_BASE_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_EMPTY_DIFF_BASE_BRANCH_COMMITS_COUNT_AS_BASE_VAR_3
  - SLASH_COMMAND_ULTRAREVIEW_EMPTY_DIFF_BASE_BRANCH_COMMITS_COUNT_AS_BASE_VAR_1
-->
Everything already committed on ${SLASH_COMMAND_ULTRAREVIEW_EMPTY_DIFF_BASE_BRANCH_COMMITS_COUNT_AS_BASE_VAR_0} counts as the base here, so only edits you haven't committed yet would be reviewed${SLASH_COMMAND_ULTRAREVIEW_EMPTY_DIFF_BASE_BRANCH_COMMITS_COUNT_AS_BASE_VAR_3>0?", and edits to those Git LFS files are not uploaded":""}. ${SLASH_COMMAND_ULTRAREVIEW_EMPTY_DIFF_BASE_BRANCH_COMMITS_COUNT_AS_BASE_VAR_1}
