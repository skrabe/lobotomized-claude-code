<!--
name: 'Tool Description: CronCreate'
description: >-
  Describes the CronCreate tool for enqueuing one-shot or recurring cron-based
  jobs with jitter and off-minute scheduling guidance
ccVersion: 2.1.144
variables:
  - CRON_DURABILITY_SECTION
  - IS_MONITOR_TOOL_ENABLED_FN
  - CRON_CREATE_TOOL_NAME
  - MONITOR_TOOL_NAME
  - CRON_DURABLE_RUNTIME_NOTE
  - CANCEL_TIMEFRAME_DAYS
  - CRON_DELETE_TOOL_NAME
-->
Schedule a prompt to be enqueued at a future time. Use for both recurring schedules and one-shot reminders.

Uses standard 5-field cron in the user's local timezone: minute hour day-of-month month day-of-week. "0 9 * * *" means 9am local — no timezone conversion needed.

## One-shot tasks (recurring: false)

For "remind me at X" or "at <time>, do Y" — fire once then auto-delete. Pin minute/hour/day-of-month/month:
  "remind me at 2:30pm today" → "30 14 <today_dom> <today_month> *", recurring: false
  "tomorrow morning, run the smoke test" → "57 8 <tomorrow_dom> <tomorrow_month> *", recurring: false

## Recurring jobs (recurring: true, the default)

  "*/5 * * * *" (every 5 min), "0 * * * *" (hourly), "0 9 * * 1-5" (weekdays at 9am local)

## Avoid the :00 and :30 minute marks when the task allows it

Everyone asking for "9am" gets \`0 9\` and everyone asking for "hourly" gets \`0 *\`, so requests from across the planet hit the API at the same instant. When the request is approximate, pick a minute that isn't 0 or 30:
  "every morning around 9" → "57 8 * * *" or "3 9 * * *"
  "hourly" → "7 * * * *"
  "in an hour or so" → whatever minute you land on; don't round

Use minute 0 or 30 only when the user names that exact time and means it ("9:00 sharp", "half past", coordinating with a meeting). When in doubt, nudge a few minutes off.

${CRON_DURABILITY_SECTION}
${IS_MONITOR_TOOL_ENABLED_FN()?`
## Not for live watching

${CRON_CREATE_TOOL_NAME} re-runs a prompt at fixed wall-clock intervals. To watch a log file, process, or command output and be notified the moment something changes, use the ${MONITOR_TOOL_NAME} tool instead — ${MONITOR_TOOL_NAME} streams events as they happen; cron polls on a schedule.
`:""}
## Runtime behavior

Jobs fire only while the REPL is idle (not mid-query). ${CRON_DURABLE_RUNTIME_NOTE}The scheduler adds a small deterministic jitter: recurring tasks fire up to 10% of their period late (max 15 min); one-shot tasks landing on :00 or :30 fire up to 90 s early. Picking an off-minute is the bigger lever.

Recurring tasks auto-expire after ${CANCEL_TIMEFRAME_DAYS} days — they fire one final time, then are deleted. Tell the user about the ${CANCEL_TIMEFRAME_DAYS}-day limit when scheduling recurring jobs.

Returns a job ID you can pass to ${CRON_DELETE_TOOL_NAME}.
