<!--
name: /copy write file failed
description: Told the model when /copy couldn't write the response to a file.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_COPY_WRITE_FAILED_VAR_0
  - SLASH_COMMAND_COPY_WRITE_FAILED_VAR_1
-->
Couldn't write the file: ${SLASH_COMMAND_COPY_WRITE_FAILED_VAR_0 instanceof SLASH_COMMAND_COPY_WRITE_FAILED_VAR_1?SLASH_COMMAND_COPY_WRITE_FAILED_VAR_0.message:SLASH_COMMAND_COPY_WRITE_FAILED_VAR_0}
