<!--
name: 'Tool Result: Cloud session — environment accepts a different repository'
description: >-
  Cloud-session create failure when the selected environment only accepts the
  repository it is set up for and the source was a different repository.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_CLOUD_SESSION_ENVIRONMENT_REPOSITORY_MISMATCH_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_ENVIRONMENT_REPOSITORY_MISMATCH_VAR_1
-->
The selected environment "${TOOL_RESULT_CLOUD_SESSION_ENVIRONMENT_REPOSITORY_MISMATCH_VAR_0}" only accepts the repository it is set up for, but the source was ${TOOL_RESULT_CLOUD_SESSION_ENVIRONMENT_REPOSITORY_MISMATCH_VAR_1}. Run this from a checkout of that repository, or select a different environment.
