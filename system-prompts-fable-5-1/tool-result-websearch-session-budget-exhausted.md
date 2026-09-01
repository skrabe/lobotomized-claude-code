<!--
name: 'Tool Result: Web Search Session Budget Exhausted'
description: >-
  Synthetic WebSearch result returned to the model once the per-session search
  cap is hit, telling it to stop issuing searches.
ccVersion: 2.1.214
variables:
  - TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_0
  - TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_1
-->
Web search was not performed: this session used its web search budget (${TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_0} of ${TOOL_RESULT_WEBSEARCH_SESSION_BUDGET_EXHAUSTED_VAR_1} WebSearch calls). Continue with the information already gathered. Ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION if more searches are needed.
