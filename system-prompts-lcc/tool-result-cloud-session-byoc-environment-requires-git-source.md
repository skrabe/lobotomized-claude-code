<!--
name: 'Tool result: cloud session BYOC environment requires git source'
description: >-
  Error when the selected environment requires a git source but no GitHub remote
  was detected.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_1
-->
${`The selected environment "${TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_0}"`} requires a git source, but no GitHub remote was detected${TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_1}. Check that \`git remote get-url origin\` returns a GitHub URL.
