<!--
name: Earlier write shadows later command
description: >-
  Command-safety approval reason surfaced to the model when a written file could
  shadow a later command under PowerShell cwd-first resolution.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_POWERSHELL_FILE_SHADOW_VAR_0
-->
An earlier sub-command writes a file (./${TOOL_RESULT_POWERSHELL_FILE_SHADOW_VAR_0}.*) that would shadow the later \`${TOOL_RESULT_POWERSHELL_FILE_SHADOW_VAR_0}\` command under Windows PowerShell 5.1 cwd-first resolution.
