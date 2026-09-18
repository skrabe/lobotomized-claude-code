<!--
name: 'Tool Result: Ripgrep Stderr Over Cap Before First Line'
description: >-
  Grep/search error when ripgrep writes more than the megabyte cap of error
  output before any result line, so the search is incomplete.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_GREP_RIPGREP_STDERR_OVER_CAP_VAR_0
-->
Ripgrep produced more than ${TOOL_RESULT_GREP_RIPGREP_STDERR_OVER_CAP_VAR_0/1e6}MB of error output (for example per-file permission warnings) before any result line, so the search is incomplete. Try a more specific path.
