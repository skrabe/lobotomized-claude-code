<!--
name: CronDelete tool description (durable)
description: Description of the cron-cancel tool (durable variant) in the tool schema.
ccVersion: 2.1.206
variables:
  - TOOL_DESCRIPTION_CRONDELETE_VAR_0
-->
Cancel a cron job previously scheduled with ${TOOL_DESCRIPTION_CRONDELETE_VAR_0}. Removes it from .claude/scheduled_tasks.json (durable jobs) or the in-memory session store (session-only jobs).
