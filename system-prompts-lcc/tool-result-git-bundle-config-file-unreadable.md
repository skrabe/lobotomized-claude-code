<!--
name: 'Git bundle: config file unreadable'
description: >-
  Refusal reason when the git configuration file cannot be read as a plain file
  or reached through a followable link
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_GIT_BUNDLE_CONFIG_FILE_UNREADABLE_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_CONFIG_FILE_UNREADABLE_VAR_1
-->
its git configuration file ${TOOL_RESULT_GIT_BUNDLE_CONFIG_FILE_UNREADABLE_VAR_0} could not be read as a plain file git would parse, or is reached through a link that cannot be followed here, so what that capture would run under cannot be judged; ${TOOL_RESULT_GIT_BUNDLE_CONFIG_FILE_UNREADABLE_VAR_1}check that file, or start from an ordinary clone
