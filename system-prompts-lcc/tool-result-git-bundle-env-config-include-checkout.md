<!--
name: Git bundle environment include in checkout
description: >-
  Explains refusal of a git environment include that a checkout session can
  modify.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_GIT_BUNDLE_ENV_CONFIG_INCLUDE_CHECKOUT_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_ENV_CONFIG_INCLUDE_CHECKOUT_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_ENV_CONFIG_INCLUDE_CHECKOUT_VAR_2
-->
its launch environment’s git configuration (GIT_CONFIG_PARAMETERS / GIT_CONFIG_COUNT) includes a file that lies inside — or links into — a git checkout (${TOOL_RESULT_GIT_BUNDLE_ENV_CONFIG_INCLUDE_CHECKOUT_VAR_0(TOOL_RESULT_GIT_BUNDLE_ENV_CONFIG_INCLUDE_CHECKOUT_VAR_1.checkout)}), which a Claude Code session started there can write; ${TOOL_RESULT_GIT_BUNDLE_ENV_CONFIG_INCLUDE_CHECKOUT_VAR_2}drop that include from the environment, keep the file outside any checkout, or start from an ordinary clone
