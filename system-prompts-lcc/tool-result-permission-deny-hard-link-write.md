<!--
name: 'Tool result: write denied on hard link'
description: >-
  Deny message when a tool tries to write a path that is a hard link to another
  file, telling the model to delete it and create a new file to reuse the name.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_PERMISSION_DENY_HARD_LINK_WRITE_VAR_0
-->
This is a hard link to ${TOOL_RESULT_PERMISSION_DENY_HARD_LINK_WRITE_VAR_0}, so a write to it could change that file; tools cannot write it. To use this name for a file of your own, delete it and create a new file
