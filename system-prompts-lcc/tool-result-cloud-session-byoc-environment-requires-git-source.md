<!--
name: 'Tool Result: Cloud Session BYOC Environment Requires Git Source'
description: >-
  onCreateFail message when the selected self-hosted (BYOC) environment needs a
  git source but no GitHub remote was detected, with a hint to check git remote
  get-url origin.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_1
  - TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_2
  - TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_3
-->
${`The selected environment "${TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_0?.TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_1??TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_2}"`} requires a git source, but no GitHub remote was detected${TOOL_RESULT_CLOUD_SESSION_BYOC_ENVIRONMENT_REQUIRES_GIT_SOURCE_VAR_3}. Check that \`git remote get-url origin\` returns a GitHub URL.
