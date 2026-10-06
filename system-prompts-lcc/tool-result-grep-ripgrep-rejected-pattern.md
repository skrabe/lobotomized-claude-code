<!--
name: 'Tool Result: Grep ripgrep rejected pattern'
description: >-
  Grep/Glob error when ripgrep rejects the pattern, glob or file type without
  searching (stderr included)
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GREP_RIPGREP_REJECTED_PATTERN_VAR_0
  - TOOL_RESULT_GREP_RIPGREP_REJECTED_PATTERN_VAR_1
-->
Search failed — ripgrep rejected the pattern, glob, or file type without searching:
${TOOL_RESULT_GREP_RIPGREP_REJECTED_PATTERN_VAR_0(TOOL_RESULT_GREP_RIPGREP_REJECTED_PATTERN_VAR_1.trim(),2000)}
