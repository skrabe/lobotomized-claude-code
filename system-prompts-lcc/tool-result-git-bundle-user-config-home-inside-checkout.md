<!--
name: 'Git bundle: home inside a checkout'
description: >-
  Refusal reason when the home directory lies inside a git checkout that can
  write user-level git config
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_INSIDE_CHECKOUT_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_INSIDE_CHECKOUT_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_INSIDE_CHECKOUT_VAR_2
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_INSIDE_CHECKOUT_VAR_3
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_INSIDE_CHECKOUT_VAR_4
-->
your home directory lies inside a git checkout (${TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_INSIDE_CHECKOUT_VAR_0(TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_INSIDE_CHECKOUT_VAR_1)}), so a Claude Code session started there can write the user-level git configuration that capture would run under (${TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_INSIDE_CHECKOUT_VAR_0(TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_INSIDE_CHECKOUT_VAR_2)}, whether or not that file exists yet); ${TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_INSIDE_CHECKOUT_VAR_3}${TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_INSIDE_CHECKOUT_VAR_4}move your home directory out of that checkout, or remove the stray git entry that makes it one
