<!--
name: 'Tool Result: Git Bundle Index Copy Rewrite Failed'
description: >-
  Failure detail, spliced into the legacy-upload refusal, when git cannot
  rewrite the private index copy as one file.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_REWRITE_FAILED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_REWRITE_FAILED_VAR_1
-->
git could not rewrite the copy as one file: ${TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_REWRITE_FAILED_VAR_0(TOOL_RESULT_GIT_BUNDLE_INDEX_COPY_REWRITE_FAILED_VAR_1.stderr)}
