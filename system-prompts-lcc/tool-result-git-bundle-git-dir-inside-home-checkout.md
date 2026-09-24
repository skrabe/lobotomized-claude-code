<!--
name: 'Git bundle: git dir inside home checkout'
description: >-
  Refusal reason when the checkout's git directory lies in a home-directory git
  checkout sessions can write
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_GIT_BUNDLE_GIT_DIR_INSIDE_HOME_CHECKOUT_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_GIT_DIR_INSIDE_HOME_CHECKOUT_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_GIT_DIR_INSIDE_HOME_CHECKOUT_VAR_2
  - TOOL_RESULT_GIT_BUNDLE_GIT_DIR_INSIDE_HOME_CHECKOUT_VAR_3
  - TOOL_RESULT_GIT_BUNDLE_GIT_DIR_INSIDE_HOME_CHECKOUT_VAR_4
-->
${TOOL_RESULT_GIT_BUNDLE_GIT_DIR_INSIDE_HOME_CHECKOUT_VAR_0(TOOL_RESULT_GIT_BUNDLE_GIT_DIR_INSIDE_HOME_CHECKOUT_VAR_1,TOOL_RESULT_GIT_BUNDLE_GIT_DIR_INSIDE_HOME_CHECKOUT_VAR_2)} and this checkout’s git directory (${TOOL_RESULT_GIT_BUNDLE_GIT_DIR_INSIDE_HOME_CHECKOUT_VAR_3(TOOL_RESULT_GIT_BUNDLE_GIT_DIR_INSIDE_HOME_CHECKOUT_VAR_2)}) is inside it, so a Claude Code session started there can write that directory’s configuration${TOOL_RESULT_GIT_BUNDLE_GIT_DIR_INSIDE_HOME_CHECKOUT_VAR_4.misplaced==="git_file"?" — start from an ordinary clone instead":""}
