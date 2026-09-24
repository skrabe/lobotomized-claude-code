<!--
name: 'Git bundle: user git config in checkout'
description: >-
  Refusal reason when the user-level git configuration lies inside or links into
  a git checkout
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_IN_CHECKOUT_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_IN_CHECKOUT_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_IN_CHECKOUT_VAR_2
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_IN_CHECKOUT_VAR_3
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_IN_CHECKOUT_VAR_4
-->
the user-level git configuration file ${TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_IN_CHECKOUT_VAR_0}, or a file it includes, lies inside — or links into — a git checkout (${TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_IN_CHECKOUT_VAR_1(TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_IN_CHECKOUT_VAR_2.checkout)}), so a Claude Code session started there can write what that capture would run under, whether or not the file exists yet; ${TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_IN_CHECKOUT_VAR_3}${TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_IN_CHECKOUT_VAR_4?"start from an ordinary clone, or ":""}keep user-level git configuration outside any checkout
