<!--
name: 'Tool result: send-to-project GitHub App not installed'
description: >-
  Warns the Claude GitHub App is not installed on the repository so threads
  cannot clone it, and to say so before the call
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_REPO_APP_NOT_INSTALLED_VAR_0
-->
 The Claude GitHub App is not installed on ${TOOL_RESULT_SEND_TO_PROJECT_REPO_APP_NOT_INSTALLED_VAR_0}. The repository can still be added, but threads need the App (https://github.com/apps/claude) to clone it. Say so before the call.
