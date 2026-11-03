<!--
name: 'Tool Result: search refused, no-follow open rejected (EINVAL)'
description: >-
  Glob/Grep refusal when the open that keeps symbolic links out of a search was
  rejected with EINVAL for the folder, suggesting a /bug report
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_SEARCH_NOFOLLOW_OPEN_REJECTED_EINVAL_VAR_0
-->
Refusing to search ${TOOL_RESULT_SEARCH_NOFOLLOW_OPEN_REJECTED_EINVAL_VAR_0}: the open that keeps symbolic links out of a search was rejected for this folder (EINVAL), so nothing was searched; other folders on the same volume may fail the same way. If this folder is on an ordinary local disk, report it with /bug.
