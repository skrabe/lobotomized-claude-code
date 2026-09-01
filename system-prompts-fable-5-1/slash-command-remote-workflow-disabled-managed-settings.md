<!--
name: 'Slash Command: Remote Workflow Disabled By Managed Settings'
description: >-
  Policy-gate refusal line explaining dynamic workflows are off via managed
  settings `disableWorkflows`; wrapped as `remote-workflow: error[policy-gate]:
  …` and returned by the __remote-workflow / workflow-launch-exec local commands
  as <local-command-stdout>, which is replayed to the model.
ccVersion: 2.1.218
-->
dynamic workflows are disabled for this session (managed settings `disableWorkflows`).
