<!--
name: PowerShell parse-error deny
description: >-
  PowerShell deny message for a parse error in a command that has a deny rule or
  may remove/hide what it runs.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_POWERSHELL_PARSE_ERROR_DENY_REWORD_VAR_0
-->
${TOOL_RESULT_POWERSHELL_PARSE_ERROR_DENY_REWORD_VAR_0.errors[0].message} It was not run, because a deny rule is set, or it may remove something or hide what it runs. To run it, reword it without that text.
