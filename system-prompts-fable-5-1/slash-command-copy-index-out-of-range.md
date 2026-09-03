<!--
name: 'Slash Command: /copy — index beyond available messages'
description: >-
  Tells the model how many assistant messages actually exist so it can pick a
  valid index instead of repeating an out-of-range one.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_COPY_INDEX_OUT_OF_RANGE_VAR_0
-->
Only ${SLASH_COMMAND_COPY_INDEX_OUT_OF_RANGE_VAR_0.length} assistant ${SLASH_COMMAND_COPY_INDEX_OUT_OF_RANGE_VAR_0.length===1?"message":"messages"} available to copy
