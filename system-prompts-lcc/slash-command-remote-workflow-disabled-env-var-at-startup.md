<!--
name: 'Remote Workflow: Disabled By Env Var At Startup'
description: >-
  Policy-gate refusal line explaining dynamic workflows are off because
  CLAUDE_CODE_DISABLE_WORKFLOWS was set when Claude Code started; wrapped as
  remote-workflow policy-gate output and replayed to the model as local-command
  stdout.
ccVersion: 2.1.285
-->
dynamic workflows are disabled for this session (the environment variable `CLAUDE_CODE_DISABLE_WORKFLOWS` was set when Claude Code started).
