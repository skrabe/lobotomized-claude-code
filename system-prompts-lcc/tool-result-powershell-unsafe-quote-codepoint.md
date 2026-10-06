<!--
name: 'Tool Result: PowerShell unsafe quote codepoint'
description: >-
  Error when a value cannot be safely single-quoted for PowerShell because it
  contains a quote-variant codepoint.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_POWERSHELL_UNSAFE_QUOTE_CODEPOINT_VAR_0
  - TOOL_RESULT_POWERSHELL_UNSAFE_QUOTE_CODEPOINT_VAR_1
-->
Cannot safely quote ${TOOL_RESULT_POWERSHELL_UNSAFE_QUOTE_CODEPOINT_VAR_0} in a PowerShell single-quoted string literal: it contains U+${TOOL_RESULT_POWERSHELL_UNSAFE_QUOTE_CODEPOINT_VAR_1}, which PowerShell's tokenizer treats as a quote delimiter
