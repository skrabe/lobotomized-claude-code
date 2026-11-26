<!--
name: 'Tool result: cloud session default env not cloud'
description: >-
  Says no cloud session started because the configured default environment is
  not a cloud one and a project cannot choose it.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_CLOUD_SESSION_DEFAULT_ENV_NOT_CLOUD_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_DEFAULT_ENV_NOT_CLOUD_VAR_1
  - TOOL_RESULT_CLOUD_SESSION_DEFAULT_ENV_NOT_CLOUD_VAR_2
  - TOOL_RESULT_CLOUD_SESSION_DEFAULT_ENV_NOT_CLOUD_VAR_3
-->
No cloud session was started: the default environment in the ${TOOL_RESULT_CLOUD_SESSION_DEFAULT_ENV_NOT_CLOUD_VAR_0(TOOL_RESULT_CLOUD_SESSION_DEFAULT_ENV_NOT_CLOUD_VAR_1)} ${TOOL_RESULT_CLOUD_SESSION_DEFAULT_ENV_NOT_CLOUD_VAR_2}, and a project cannot choose that. To use another environment, remove remote.defaultEnvironmentId from those settings.${TOOL_RESULT_CLOUD_SESSION_DEFAULT_ENV_NOT_CLOUD_VAR_3?"":" To start there, choose it yourself with /remote-env in an interactive session."}
