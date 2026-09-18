<!--
name: 'Slash Command: Ultrareview Not A Git Repo (cd or init)'
description: >-
  Remedy tail of the ultrareview not_git_repo precondition error: cd into the
  project if it already uses git and rerun, otherwise git init and commit.
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_ULTRAREVIEW_NOT_GIT_REPO_CD_OR_INIT_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_NOT_GIT_REPO_CD_OR_INIT_VAR_1
-->
If your project already uses git, cd into its folder and rerun ${SLASH_COMMAND_ULTRAREVIEW_NOT_GIT_REPO_CD_OR_INIT_VAR_0}. If it doesn't yet, ${SLASH_COMMAND_ULTRAREVIEW_NOT_GIT_REPO_CD_OR_INIT_VAR_1}
