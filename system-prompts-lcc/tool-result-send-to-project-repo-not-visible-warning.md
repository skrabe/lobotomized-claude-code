<!--
name: 'Tool result: send-to-project repository not visible to account'
description: >-
  Warns the Claude account cannot see the GitHub repository so threads cannot
  clone it, and to say so before the call
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_REPO_NOT_VISIBLE_WARNING_VAR_0
-->
 Their Claude account cannot see ${TOOL_RESULT_SEND_TO_PROJECT_REPO_NOT_VISIBLE_WARNING_VAR_0} (the GitHub account connected at claude.ai may differ). The repository can still be added, but threads cannot clone it until that is fixed. Say so before the call.
