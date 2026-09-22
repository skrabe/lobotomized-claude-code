<!--
name: 'Tool Result: Agent Budget Limit Reached'
description: >-
  AgentPreconditionError thrown inside the Task tool's call() when maxBudgetUsd
  is exhausted; returned to the model as the tool's error result telling it to
  finish the work without spawning agents.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_TASK_BUDGET_LIMIT_REACHED_VAR_0
  - TOOL_RESULT_TASK_BUDGET_LIMIT_REACHED_VAR_1
-->
Budget limit reached ($${TOOL_RESULT_TASK_BUDGET_LIMIT_REACHED_VAR_0().toFixed(2)} spent of the $${TOOL_RESULT_TASK_BUDGET_LIMIT_REACHED_VAR_1} maximum). New agents cannot be started — complete the remaining work directly with your tools.
