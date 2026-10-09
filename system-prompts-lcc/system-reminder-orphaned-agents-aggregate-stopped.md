<!--
name: Aggregate orphaned agents (stopped) notice
description: >-
  Aggregate-summary fragment injected into model context stating orphaned tasks
  may have been stopped or running at exit.
ccVersion: 2.1.295
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_STOPPED_VAR_0
  - SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_STOPPED_VAR_1
-->
They may have been ${SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_STOPPED_VAR_0==="workflow"?SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_STOPPED_VAR_1:"stopped (via the UI, Monitor timeout, or agent teardown — these leave no transcript marker)"}, or they may have been running when the previous Claude Code process exited. They have been marked stopped.
