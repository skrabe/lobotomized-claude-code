<!--
name: 'Tool result: WebSearch budget limit with refill'
description: >-
  Limit clause of the WebSearch budget-exhausted result when the budget refills
  at an hourly rate.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WEBSEARCH_BUDGET_LIMIT_REFILLS_VAR_0
  - TOOL_RESULT_WEBSEARCH_BUDGET_LIMIT_REFILLS_VAR_1
  - TOOL_RESULT_WEBSEARCH_BUDGET_LIMIT_REFILLS_VAR_2
  - TOOL_RESULT_WEBSEARCH_BUDGET_LIMIT_REFILLS_VAR_3
-->
limit: ${TOOL_RESULT_WEBSEARCH_BUDGET_LIMIT_REFILLS_VAR_0} shared by every agent in this ${TOOL_RESULT_WEBSEARCH_BUDGET_LIMIT_REFILLS_VAR_1}; the budget refills at about ${TOOL_RESULT_WEBSEARCH_BUDGET_LIMIT_REFILLS_VAR_2} ${TOOL_RESULT_WEBSEARCH_BUDGET_LIMIT_REFILLS_VAR_3(TOOL_RESULT_WEBSEARCH_BUDGET_LIMIT_REFILLS_VAR_2,"call")} per hour, so searching becomes possible again later in the ${TOOL_RESULT_WEBSEARCH_BUDGET_LIMIT_REFILLS_VAR_1}
