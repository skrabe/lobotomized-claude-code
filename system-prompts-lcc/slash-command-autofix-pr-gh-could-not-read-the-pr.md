<!--
name: 'Slash Command: /autofix-pr failure reason: gh could not read the pr'
description: 'Failure reason clause of /autofix-pr: "gh couldn''t read the PR: ${||}"'
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_AUTOFIX_PR_GH_COULD_NOT_READ_THE_PR_VAR_0
  - SLASH_COMMAND_AUTOFIX_PR_GH_COULD_NOT_READ_THE_PR_VAR_1
-->
gh couldn't read the PR: ${SLASH_COMMAND_AUTOFIX_PR_GH_COULD_NOT_READ_THE_PR_VAR_0||SLASH_COMMAND_AUTOFIX_PR_GH_COULD_NOT_READ_THE_PR_VAR_1}
