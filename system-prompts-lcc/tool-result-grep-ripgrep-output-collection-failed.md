<!--
name: 'Tool Result: Grep Ripgrep Output Collection Failed'
description: >-
  Grep/search tool error returned to the model when collecting ripgrep
  stdout/stderr fails, often because the match set is huge.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_GREP_RIPGREP_OUTPUT_COLLECTION_FAILED_VAR_0
-->
Failed to collect ripgrep output: ${TOOL_RESULT_GREP_RIPGREP_OUTPUT_COLLECTION_FAILED_VAR_0.message}. If the search matches a very large amount of text, try a more specific path or pattern.
