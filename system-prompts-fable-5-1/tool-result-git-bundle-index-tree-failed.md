<!--
name: Index Tree Failed
description: >-
  Cloud-session creation failure telling the model the legacy upload's private
  index copy could not be used.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_INDEX_TREE_FAILED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_INDEX_TREE_FAILED_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_INDEX_TREE_FAILED_VAR_2
  - TOOL_RESULT_GIT_BUNDLE_INDEX_TREE_FAILED_VAR_3
-->
It is not uploaded the previous way either: that way runs only over a private copy of this checkout's index, and ${TOOL_RESULT_GIT_BUNDLE_INDEX_TREE_FAILED_VAR_0(TOOL_RESULT_GIT_BUNDLE_INDEX_TREE_FAILED_VAR_1(TOOL_RESULT_GIT_BUNDLE_INDEX_TREE_FAILED_VAR_2.detail),TOOL_RESULT_GIT_BUNDLE_INDEX_TREE_FAILED_VAR_3)}. Nothing was uploaded; once that is put right, retry, or start from an ordinary clone.
