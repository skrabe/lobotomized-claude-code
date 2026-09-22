<!--
name: 'Tool Result: Git Bundle Config File Hard Link'
description: >-
  pC clause when a named git config file, or a file it includes, has a second
  hard-link name.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_CONFIG_FILE_HARD_LINK_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_CONFIG_FILE_HARD_LINK_VAR_1
-->
its git configuration file ${TOOL_RESULT_GIT_BUNDLE_CONFIG_FILE_HARD_LINK_VAR_0} (or a file it includes) has a second name — a hard link — so a session that can reach the other name could change what that capture runs under; ${TOOL_RESULT_GIT_BUNDLE_CONFIG_FILE_HARD_LINK_VAR_1}give the file a single name again (copy it aside and move the copy back over it), or start from an ordinary clone
