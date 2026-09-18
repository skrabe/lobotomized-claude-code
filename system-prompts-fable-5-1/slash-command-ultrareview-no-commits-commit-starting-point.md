<!--
name: 'Slash Command: Ultrareview Branch Has No Commits (Commit Starting Point)'
description: >-
  Ultrareview no_merge_base precondition error when HEAD has no commits and the
  caller does not confirm before launch: commit a starting point first, then the
  review covers changes made on top of it.
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_ULTRAREVIEW_NO_COMMITS_COMMIT_STARTING_POINT_VAR_0
-->
Your current branch has no commits yet, so there is nothing to review. Commit a starting point first. ${SLASH_COMMAND_ULTRAREVIEW_NO_COMMITS_COMMIT_STARTING_POINT_VAR_0} then reviews the changes you make on top of that commit.
