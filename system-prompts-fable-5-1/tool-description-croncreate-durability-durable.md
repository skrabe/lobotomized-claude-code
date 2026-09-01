<!--
name: CronCreate durability note (durable)
description: >-
  Durable-job durability explanation within the cron tool description sent to
  the model.
ccVersion: 2.1.206
-->
Durable jobs persist to .claude/scheduled_tasks.json and survive session restarts — on next launch they resume automatically. One-shot durable tasks that were missed while the REPL was closed are surfaced for catch-up.
