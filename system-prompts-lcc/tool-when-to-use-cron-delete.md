<!--
name: 'Tool whenToUse: CronDelete'
description: >-
  Deferred-tool listing line telling Claude to cancel session cron jobs with
  this tool, not by editing scheduled_tasks.json.
ccVersion: 2.1.325
variables:
  - TOOL_WHEN_TO_USE_CRON_DELETE_VAR_0
-->
When you are about to stop a job that ${TOOL_WHEN_TO_USE_CRON_DELETE_VAR_0} scheduled, use it and not an edit of .claude/scheduled_tasks.json, which does not hold session-only jobs.
