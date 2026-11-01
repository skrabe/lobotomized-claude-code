<!--
name: 'Slash command: ultrareview needs GitHub remote to clone'
description: >-
  Ultrareview precondition error that a GitHub remote is needed to clone the
  repo into the cloud, with git remote add/push command.
ccVersion: 2.1.316
variables:
  - SLASH_COMMAND_ULTRAREVIEW_NEEDS_GITHUB_REMOTE_CLONE_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_NEEDS_GITHUB_REMOTE_CLONE_VAR_1
-->
${SLASH_COMMAND_ULTRAREVIEW_NEEDS_GITHUB_REMOTE_CLONE_VAR_0} needs a GitHub remote so it can clone this repository into the cloud. ${SLASH_COMMAND_ULTRAREVIEW_NEEDS_GITHUB_REMOTE_CLONE_VAR_1} If a GitHub repo already exists, run \`git remote add origin REPO_URL && git push -u origin HEAD\`.
