<!--
name: Search Symlink Resolution Changed
description: >-
  Glob/Grep tool error when a search path's symlink resolution changed after the
  permission check, returned to the model as the tool result.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_SEARCH_SYMLINK_RESOLUTION_CHANGED_VAR_0
-->
Refusing to search ${TOOL_RESULT_SEARCH_SYMLINK_RESOLUTION_CHANGED_VAR_0}: its symlink resolution changed after permission was checked. If a link in the working directory is being rewritten concurrently, stop that and retry.
