<!--
name: 'Git bundle: home is a checkout'
description: >-
  Refusal reason when the home directory itself is a git checkout that can write
  user-level git config
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_IS_CHECKOUT_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_IS_CHECKOUT_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_IS_CHECKOUT_VAR_2
  - TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_IS_CHECKOUT_VAR_3
-->
your home directory is itself a git checkout, so a Claude Code session started there can write the user-level git configuration that capture would run under (${TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_IS_CHECKOUT_VAR_0(TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_IS_CHECKOUT_VAR_1)}, whether or not that file exists yet); ${TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_IS_CHECKOUT_VAR_2}${TOOL_RESULT_GIT_BUNDLE_USER_CONFIG_HOME_IS_CHECKOUT_VAR_3}keep the dotfiles repository’s git directory outside your home (a bare repository used with --git-dir)
