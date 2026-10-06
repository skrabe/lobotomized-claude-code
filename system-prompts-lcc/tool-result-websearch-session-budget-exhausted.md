<!--
name: 'Tool Result: Web Search Session Budget Exhausted'
description: >-
  Synthetic WebSearch result returned to the model once the per-session search
  cap is hit, telling it to stop issuing searches.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_0
  - TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_1
  - TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_2
  - TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_3
  - TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_4
-->
Web search was not performed: this ${TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_0}'s web search budget is used up (${TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_1}). ${TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_2}; do not work around the limit by querying search engines with curl or wget from ${TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_3}, or by searching or fetching through a third-party reader, proxy or archive service.${TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_4}
