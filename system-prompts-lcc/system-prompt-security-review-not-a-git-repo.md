<!--
name: 'System Prompt: /security-review not a git repo'
description: >-
  security-review slash-command prompt returned when cwd is not a git
  repository, instructing the model to tell the user
ccVersion: 2.1.178
variables:
  - SYSTEM_PROMPT_SECURITY_REVIEW_NOT_A_GIT_REPO_VAR_0
-->
Tell the user that /security-review must run inside a git repository, but the current working directory (\`${SYSTEM_PROMPT_SECURITY_REVIEW_NOT_A_GIT_REPO_VAR_0}\`) is not one. If the repo is in a subdirectory, `cd` into it and re-run. If this is a self-hosted runner session created without a `git_repository` source, add one at session creation (so the runner clones it and sets the working directory) or `cd` into the cloned repo before running.
