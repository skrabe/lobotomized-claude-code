<!--
name: 'Tool Result: Git Bundle Git Dir Under Temp'
description: >-
  Previous-way clause refusing the upload when .git names a git directory that
  sits under a temporary directory.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_GIT_DIR_UNDER_TEMP_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_GIT_DIR_UNDER_TEMP_VAR_1
-->
its .git file names a git directory under a temporary directory (${TOOL_RESULT_GIT_BUNDLE_GIT_DIR_UNDER_TEMP_VAR_0(TOOL_RESULT_GIT_BUNDLE_GIT_DIR_UNDER_TEMP_VAR_1.gitDir)}), where sessions write — start from an ordinary clone of the repository
