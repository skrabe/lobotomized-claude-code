<!--
name: Environment Info Git Repo Changed
description: >-
  Environment-update prompt line reporting whether the primary directory is a
  git repository after a change.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_ENV_INFO_GIT_REPO_CHANGED_VAR_0
-->
Is a git repository: ${SYSTEM_PROMPT_ENV_INFO_GIT_REPO_CHANGED_VAR_0.isGitRepo} (was ${!SYSTEM_PROMPT_ENV_INFO_GIT_REPO_CHANGED_VAR_0.isGitRepo})
