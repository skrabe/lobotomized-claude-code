<!--
name: Private Git Dir Home
description: >-
  Cloud-session creation failure telling the model the private git directory
  under the config home could not be prepared.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_2
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_3
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_4
-->
Could not prepare a private git directory for the upload (${TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_0}), so nothing was uploaded. It is kept under your configuration home: check that ${TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_1(TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_2.home)} is a writable directory of yours, and that ${TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_1(TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_3(TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_2.home,"seed-admin"))}, if it exists, is a directory only you can write. Look at it first: ls -ld, with no / after the name (tab completion adds one, and with it a link to a folder shows as a plain folder). A directory there holds scratch only and can be removed (rm -r, again with no /). A link or a file there is removed by its name (rm, with no -r and no / after the name). Then retry.${TOOL_RESULT_GIT_BUNDLE_PRIVATE_DIR_HOME_VAR_4}
