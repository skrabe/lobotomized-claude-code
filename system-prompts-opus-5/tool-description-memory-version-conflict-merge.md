<!--
name: 'Tool Description: Memory version conflict merge guidance'
description: >-
  Second version-tokens paragraph of the memory_write prompt explaining that a
  rejected write returns the current content to merge and retry.
ccVersion: 2.1.224
variables:
  - TOOL_DESCRIPTION_MEMORY_VERSION_CONFLICT_MERGE_VAR_0
-->
If the document changed since you read it, or you pass new for a path that already exists, the write is rejected and returns the current content (when it is within the read cap) and its version — merge your change into that content and call ${TOOL_DESCRIPTION_MEMORY_VERSION_CONFLICT_MERGE_VAR_0} again with the returned version.
