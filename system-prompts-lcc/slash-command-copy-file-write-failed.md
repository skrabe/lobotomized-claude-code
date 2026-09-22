<!--
name: 'Slash Command: /copy — file write failed'
description: >-
  Tells the model the write-to-file shortcut failed and carries the underlying
  error, so the model knows no file exists and why.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_COPY_FILE_WRITE_FAILED_VAR_0
  - SLASH_COMMAND_COPY_FILE_WRITE_FAILED_VAR_1
-->
Failed to write file: ${SLASH_COMMAND_COPY_FILE_WRITE_FAILED_VAR_0 instanceof SLASH_COMMAND_COPY_FILE_WRITE_FAILED_VAR_1?SLASH_COMMAND_COPY_FILE_WRITE_FAILED_VAR_0.message:SLASH_COMMAND_COPY_FILE_WRITE_FAILED_VAR_0}
