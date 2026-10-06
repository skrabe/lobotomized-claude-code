<!--
name: 'Tool Result: Git bundle git step failed'
description: >-
  Generic bundle error naming the failed git command, its exit code and stderr,
  optionally suggesting git fsck
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_GIT_STEP_FAILED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_GIT_STEP_FAILED_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_GIT_STEP_FAILED_VAR_2
  - TOOL_RESULT_GIT_BUNDLE_GIT_STEP_FAILED_VAR_3
-->
${TOOL_RESULT_GIT_BUNDLE_GIT_STEP_FAILED_VAR_0} failed (${TOOL_RESULT_GIT_BUNDLE_GIT_STEP_FAILED_VAR_1.code})${TOOL_RESULT_GIT_BUNDLE_GIT_STEP_FAILED_VAR_2&&`: ${TOOL_RESULT_GIT_BUNDLE_GIT_STEP_FAILED_VAR_2}`}${TOOL_RESULT_GIT_BUNDLE_GIT_STEP_FAILED_VAR_3?"; `git fsck` in this checkout may show why":""}
