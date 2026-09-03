<!--
name: 'Slash Command: /low-priority budget exhausted'
description: >-
  /low-priority output when lower-priority mode is unavailable because the
  weekly budget is exhausted, saying the mode is offered again after the weekly
  limit resets
ccVersion: 2.1.239
variables:
  - SLASH_COMMAND_LOW_PRIORITY_BUDGET_EXHAUSTED_VAR_0
-->
${SLASH_COMMAND_LOW_PRIORITY_BUDGET_EXHAUSTED_VAR_0().budgetExhaustedCopy}. Lower-priority mode is offered again after your weekly limit resets.
