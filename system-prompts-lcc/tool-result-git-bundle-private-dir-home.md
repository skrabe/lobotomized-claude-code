<!--
name: Private Git Dir Home
description: >-
  Cloud-session creation failure telling the model the private git directory
  under the config home could not be prepared.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_2
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_3
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_4
-->
Could not prepare a private git directory for the upload (${TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_0}), so nothing was uploaded. It is kept under your configuration home: check that ${TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_1(TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_2.home)} is a writable directory of yours, and that ${TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_1(TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_3(TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_2.home,"seed-admin"))}, if it stands, is a directory only you can write — look at it first (ls -ld): a directory there holds scratch only and can be removed; a link or a file at that name is removed by name (rm, no trailing slash); then retry.${TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_4}
