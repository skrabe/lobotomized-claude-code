<!--
name: Command has unparsable malformed syntax
description: >-
  PowerShell command-safety reason surfaced to the model when the command cannot
  be parsed.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_POWERSHELL_MALFORMED_SYNTAX_VAR_0
  - TOOL_RESULT_POWERSHELL_MALFORMED_SYNTAX_VAR_1
-->
Command contains malformed syntax that cannot be parsed: ${TOOL_RESULT_POWERSHELL_MALFORMED_SYNTAX_VAR_0.errors[0]?.TOOL_RESULT_POWERSHELL_MALFORMED_SYNTAX_VAR_1??"unknown error"}
