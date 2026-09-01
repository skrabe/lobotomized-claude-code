<!--
name: Missed one-shot scheduled tasks notice
description: >-
  Reminder injected into model context that missed one-shot scheduled tasks were
  removed and must be confirmed via AskUserQuestion before running.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_MISSED_SCHEDULED_TASKS_VAR_0
-->
The following one-shot scheduled task${SYSTEM_REMINDER_MISSED_SCHEDULED_TASKS_VAR_0?"s were":" was"} missed while Claude was not running. ${SYSTEM_REMINDER_MISSED_SCHEDULED_TASKS_VAR_0?"They have":"It has"} already been removed from .claude/scheduled_tasks.json.

First use the AskUserQuestion tool to ask whether to run ${SYSTEM_REMINDER_MISSED_SCHEDULED_TASKS_VAR_0?"each one":"it"} now. Only execute if the user confirms.
