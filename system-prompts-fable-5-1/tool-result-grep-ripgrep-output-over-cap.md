<!--
name: 'Tool Result: Ripgrep Output Over Cap Before First Line'
description: >-
  Grep/search error when ripgrep stdout exceeds the megabyte cap before a
  complete line, so there are no usable results.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_GREP_RIPGREP_OUTPUT_OVER_CAP_VAR_0
-->
Ripgrep output passed the ${TOOL_RESULT_GREP_RIPGREP_OUTPUT_OVER_CAP_VAR_0/1e6}MB limit before a single complete line was read, so there are no usable results: at least one matching line is extremely long. Try a more specific pattern or path, or exclude very large files.
