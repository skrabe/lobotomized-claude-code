<!--
name: Index Copy Failed
description: >-
  Cloud-session creation failure telling the model the legacy upload could not
  make a private index copy.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_FAILED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_FAILED_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_FAILED_VAR_2
  - TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_FAILED_VAR_3
-->
It is not uploaded the previous way either: a private copy of this checkout's index could not be made (${TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_FAILED_VAR_0(TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_FAILED_VAR_1(TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_FAILED_VAR_2.detail),TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_FAILED_VAR_3)}), and that way runs only over such a copy. Nothing was uploaded; once that is put right, retry, or start from an ordinary clone.
