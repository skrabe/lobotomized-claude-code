<!--
name: 'Skill: Schedule recurring cron and execute immediately (compact)'
description: >-
  Instructions for creating a recurring cron job, confirming the schedule with
  the user, and immediately executing the parsed prompt without waiting for the
  first cron fire
ccVersion: 2.1.101
variables:
  - CRON_CREATE_TOOL_NAME
  - CANCEL_TIMEFRAME_DAYS
  - CRON_DELETE_TOOL_NAME
  - ADDITIONAL_INFO_FN
-->
1. Call ${CRON_CREATE_TOOL_NAME} with: \`cron\` (the expression above), \`prompt\` (the parsed prompt verbatim), \`recurring: true\`.
2. Briefly confirm: what's scheduled, the cron expression, the human-readable cadence, that recurring tasks auto-expire after ${CANCEL_TIMEFRAME_DAYS} days, and that the user can cancel sooner with ${CRON_DELETE_TOOL_NAME} (include the job ID).${ADDITIONAL_INFO_FN()}
3. **Then immediately execute the parsed prompt now** — don't wait for the first cron fire. If it's a slash command, invoke it via the Skill tool; otherwise act on it directly.
