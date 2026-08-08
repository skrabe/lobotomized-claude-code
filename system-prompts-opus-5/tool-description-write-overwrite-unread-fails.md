<!--
name: 'Tool Description: Write overwrite-unread warning'
description: >-
  Optional sentence appended to the Write tool description warning that
  overwriting a file the model has not Read will fail; included when the
  read-before-write gate is active.
ccVersion: 2.1.224
variables:
  - TOOL_DESCRIPTION_WRITE_OVERWRITE_UNREAD_FAILS_VAR_0
-->
 Overwriting an existing file you haven't ${TOOL_DESCRIPTION_WRITE_OVERWRITE_UNREAD_FAILS_VAR_0} will fail.
