<!--
name: Permission handler narrowed the input
description: >-
  Result returned to Claude when the permission handler rewrote a peer-send
  input into a shape the tool does not accept, so nothing was sent; now shared
  by SendMessage and SendFile.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_SENDFILE_PERMISSION_NARROWED_INPUT_VAR_0
-->
The permission handler narrowed the input to a shape ${TOOL_RESULT_SENDFILE_PERMISSION_NARROWED_INPUT_VAR_0.name} does not accept — nothing was sent.
