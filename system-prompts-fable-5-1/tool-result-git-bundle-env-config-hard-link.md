<!--
name: 'Tool Result: Git Bundle Env Config Hard Link'
description: >-
  pC clause when GIT_CONFIG_PARAMETERS includes a file that has a second
  hard-link name.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_ENV_CONFIG_HARD_LINK_VAR_0
-->
its launch environment’s git configuration (GIT_CONFIG_PARAMETERS / GIT_CONFIG_COUNT) includes a file that has a second name — a hard link — so a session that can reach the other name could change what that capture runs under; ${TOOL_RESULT_GIT_BUNDLE_ENV_CONFIG_HARD_LINK_VAR_0}give that file a single name again (copy it aside and move the copy back over it), drop that include from the environment, or start from an ordinary clone
