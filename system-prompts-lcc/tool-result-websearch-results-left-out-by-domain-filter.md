<!--
name: 'Tool Result: WebSearch results left out by domain filter'
description: Counts search results left out by allowed_domains or blocked_domains
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_WEBSEARCH_RESULTS_LEFT_OUT_BY_DOMAIN_FILTER_VAR_0
  - TOOL_RESULT_WEBSEARCH_RESULTS_LEFT_OUT_BY_DOMAIN_FILTER_VAR_1
-->
${TOOL_RESULT_WEBSEARCH_RESULTS_LEFT_OUT_BY_DOMAIN_FILTER_VAR_0.leftOut} ${TOOL_RESULT_WEBSEARCH_RESULTS_LEFT_OUT_BY_DOMAIN_FILTER_VAR_1(TOOL_RESULT_WEBSEARCH_RESULTS_LEFT_OUT_BY_DOMAIN_FILTER_VAR_0.leftOut,"result")} left out by allowed_domains or blocked_domains.
