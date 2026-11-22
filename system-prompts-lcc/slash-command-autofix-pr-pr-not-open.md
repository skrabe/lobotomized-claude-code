<!--
name: /autofix-pr PR not open
description: Tells the model the PR is merged or closed and autofix needs an open PR.
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_AUTOFIX_PR_PR_NOT_OPEN_VAR_0
-->
PR #${SLASH_COMMAND_AUTOFIX_PR_PR_NOT_OPEN_VAR_0.number} is ${SLASH_COMMAND_AUTOFIX_PR_PR_NOT_OPEN_VAR_0.state.toLowerCase()}. Autofix requires an open PR.
