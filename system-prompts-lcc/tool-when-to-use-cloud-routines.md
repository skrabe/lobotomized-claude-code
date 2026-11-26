<!--
name: 'Tool whenToUse: Cloud routines'
description: >-
  Deferred-tool listing line telling Claude to use claude.ai routines for jobs
  that must run while Claude Code is closed, not session cron.
ccVersion: 2.1.332
variables:
  - TOOL_WHEN_TO_USE_CLOUD_ROUTINES_VAR_0
-->
When a job must run on a schedule or event while Claude Code is closed, or you will create, change, run or debug a cloud scheduled task (routine), use it and not ${TOOL_WHEN_TO_USE_CLOUD_ROUTINES_VAR_0}, which runs only while Claude Code does.
