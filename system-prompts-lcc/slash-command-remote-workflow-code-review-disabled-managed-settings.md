<!--
name: 'Remote Workflow: Code Review Disabled By Managed Settings'
description: >-
  Policy-gate refusal for review-origin workflow launches when managed settings
  turn workflows off (disableWorkflows or CLAUDE_CODE_DISABLE_WORKFLOWS in env);
  returned as the policy-gate line of the workflow-launch-exec local command
  output replayed to the model.
ccVersion: 2.1.285
-->
Code review did not run: workflows are turned off in this machine's managed settings (`disableWorkflows`, or `CLAUDE_CODE_DISABLE_WORKFLOWS` in its `env` block). Ask this machine's administrator to allow it.
