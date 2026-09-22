<!--
name: 'Tool Result: Git Bundle Forged Index Paths'
description: >-
  Refuses the teleport git-bundle upload when git reports changed paths spelled
  in a way git itself never writes, so the checkout's index or HEAD was edited
  by something other than git.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_GIT_BUNDLE_FORGED_INDEX_PATHS_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_FORGED_INDEX_PATHS_VAR_1
-->
Not uploading this working tree: git reports changed paths spelled in a way git itself never writes (${TOOL_RESULT_GIT_BUNDLE_FORGED_INDEX_PATHS_VAR_0(TOOL_RESULT_GIT_BUNDLE_FORGED_INDEX_PATHS_VAR_1)}), so this checkout's index or HEAD was edited by something other than git. Inspect it (git status, git log) before retrying.
