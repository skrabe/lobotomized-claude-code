<!--
name: 'Tool result: cloud session selected env not hosted'
description: >-
  Says no cloud session started because Claude-started sessions run only on
  hosted or self-hosted environments, with /remote-env guidance.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_CLOUD_SESSION_SELECTED_ENV_NOT_HOSTED_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_SELECTED_ENV_NOT_HOSTED_VAR_1
-->
No cloud session was started: a session that Claude starts runs only on a hosted or self-hosted environment, and the selected one ${TOOL_RESULT_CLOUD_SESSION_SELECTED_ENV_NOT_HOSTED_VAR_0}. To choose a cloud environment, the person can run /remote-env in an interactive session, unless their organization or --settings set this default. If /remote-env lists no cloud environment, they can create one at ${TOOL_RESULT_CLOUD_SESSION_SELECTED_ENV_NOT_HOSTED_VAR_1}.
