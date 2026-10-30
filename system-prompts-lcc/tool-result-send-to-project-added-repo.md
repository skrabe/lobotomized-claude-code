<!--
name: 'Tool result: Send to project added repository'
description: >-
  Result line naming the GitHub repository added to the project, with an
  optional GitHub App install note.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_ADDED_REPO_VAR_0
-->
Added github.com/${TOOL_RESULT_SEND_TO_PROJECT_ADDED_REPO_VAR_0.attachedRepo}.${TOOL_RESULT_SEND_TO_PROJECT_ADDED_REPO_VAR_0.appInstallPending?" Install the [Claude GitHub App](https://github.com/apps/claude) on it so threads can clone it.":""}
