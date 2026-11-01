<!--
name: 'Slash command: ultrareview PR needs GitHub remote'
description: >-
  Ultrareview error that reviewing a PR number needs a GitHub remote, with how
  to add one or review the current branch.
ccVersion: 2.1.316
variables:
  - SLASH_COMMAND_ULTRAREVIEW_PR_NEEDS_GITHUB_REMOTE_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_PR_NEEDS_GITHUB_REMOTE_VAR_1
-->
${SLASH_COMMAND_ULTRAREVIEW_PR_NEEDS_GITHUB_REMOTE_VAR_0} <PR#> needs a GitHub remote so it knows which repository the PR is in. ${SLASH_COMMAND_ULTRAREVIEW_PR_NEEDS_GITHUB_REMOTE_VAR_1} If a GitHub repo already exists, run \`git remote add origin REPO_URL\`. Or run ${SLASH_COMMAND_ULTRAREVIEW_PR_NEEDS_GITHUB_REMOTE_VAR_0} with no argument to review your current branch instead.
