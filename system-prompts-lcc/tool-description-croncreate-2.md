<!--
name: CronCreate tool description (durable)
description: >-
  Durable-variant description of the cron scheduling tool in the model's tool
  schema.
ccVersion: 2.1.330
-->
Schedule a prompt to run at a future time — either recurring on a cron schedule, or once at a specific time. Pass durable: true to save it to .claude/scheduled_tasks.json where that is possible; otherwise session-only.
