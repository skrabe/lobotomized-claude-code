<!--
name: 'Remote Workflow: Disabled By Env Var Set After Startup'
description: >-
  Policy-gate refusal line explaining dynamic workflows are off because
  CLAUDE_CODE_DISABLE_WORKFLOWS was set after Claude Code started (for example
  by a settings env block); replayed to the model as remote-workflow policy-gate
  output.
ccVersion: 2.1.285
-->
dynamic workflows are disabled for this session (the environment variable `CLAUDE_CODE_DISABLE_WORKFLOWS`, set after Claude Code started, for example by a settings `env` block).
