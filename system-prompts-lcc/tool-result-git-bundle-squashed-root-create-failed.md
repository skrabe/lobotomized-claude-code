<!--
name: 'Tool Result: Git Bundle Squashed Root Create Failed'
description: >-
  Bundle-failure result when git bundle create for the squashed root commit
  fails, including the git exit code and stderr.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_GIT_BUNDLE_SQUASHED_ROOT_CREATE_FAILED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_SQUASHED_ROOT_CREATE_FAILED_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_SQUASHED_ROOT_CREATE_FAILED_VAR_2
-->
git bundle create for the squashed root failed (${TOOL_RESULT_GIT_BUNDLE_SQUASHED_ROOT_CREATE_FAILED_VAR_0.code}): ${TOOL_RESULT_GIT_BUNDLE_SQUASHED_ROOT_CREATE_FAILED_VAR_1(TOOL_RESULT_GIT_BUNDLE_SQUASHED_ROOT_CREATE_FAILED_VAR_0.stderr,TOOL_RESULT_GIT_BUNDLE_SQUASHED_ROOT_CREATE_FAILED_VAR_2)}
