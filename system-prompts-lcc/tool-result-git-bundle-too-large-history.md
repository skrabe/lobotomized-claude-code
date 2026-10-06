<!--
name: 'Tool Result: Git bundle too large history'
description: >-
  Error that the repository is too large to upload because its git history
  exceeds the upload limit
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_TOO_LARGE_HISTORY_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_TOO_LARGE_HISTORY_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_TOO_LARGE_HISTORY_VAR_2
-->
This repository is too large to upload: its git history is ${TOOL_RESULT_GIT_BUNDLE_TOO_LARGE_HISTORY_VAR_0(TOOL_RESULT_GIT_BUNDLE_TOO_LARGE_HISTORY_VAR_1)}, and an upload can be at most ${TOOL_RESULT_GIT_BUNDLE_TOO_LARGE_HISTORY_VAR_0(TOOL_RESULT_GIT_BUNDLE_TOO_LARGE_HISTORY_VAR_2.maxBytes)}
