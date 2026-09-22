<!--
name: 'Slash Command: /ultrareview — Not Inside A Git Repository'
description: >-
  Error explaining that the review compares a git branch against an earlier
  commit but the current directory is not inside a git repository, followed by
  the remediation advice.
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_ULTRAREVIEW_NOT_GIT_REPO_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_NOT_GIT_REPO_VAR_1
  - SLASH_COMMAND_ULTRAREVIEW_NOT_GIT_REPO_VAR_2
-->
${SLASH_COMMAND_ULTRAREVIEW_NOT_GIT_REPO_VAR_0} reviews the changes a git branch makes on top of an earlier commit, but ${SLASH_COMMAND_ULTRAREVIEW_NOT_GIT_REPO_VAR_1()} is not inside a git repository. ${SLASH_COMMAND_ULTRAREVIEW_NOT_GIT_REPO_VAR_2}
