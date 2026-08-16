<!--
name: 'Slash Command: /export — export failed'
description: >-
  Tells the model the export never wrote a file and why, so it does not go on to
  reference a nonexistent path.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_EXPORT_FAILED_VAR_0
  - SLASH_COMMAND_EXPORT_FAILED_VAR_1
-->
Failed to export conversation: ${SLASH_COMMAND_EXPORT_FAILED_VAR_0 instanceof SLASH_COMMAND_EXPORT_FAILED_VAR_1?SLASH_COMMAND_EXPORT_FAILED_VAR_0.message:"Unknown error"}
