<!--
name: 'Tool Result: WebFetch verbatim text cutoff'
description: >-
  Marks where the verbatim page text stops and that re-fetching the URL (at the
  same offset) returns the same split
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WEBFETCH_VERBATIM_TEXT_CUTOFF_VAR_0
  - TOOL_RESULT_WEBFETCH_VERBATIM_TEXT_CUTOFF_VAR_1
  - TOOL_RESULT_WEBFETCH_VERBATIM_TEXT_CUTOFF_VAR_2
-->
[The verbatim page text stops here, ${TOOL_RESULT_WEBFETCH_VERBATIM_TEXT_CUTOFF_VAR_0} of ${TOOL_RESULT_WEBFETCH_VERBATIM_TEXT_CUTOFF_VAR_1.length} characters in; re-fetching this URL${TOOL_RESULT_WEBFETCH_VERBATIM_TEXT_CUTOFF_VAR_2&&" at the same offset"} returns the same split.
