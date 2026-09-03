<!--
name: 'Tool Result: Spawn local runner ask message'
description: >-
  The spawn-local-runner tool's ask-permission message; not rendered by the
  permission dialog, so it reaches the model as the tool_result content when the
  ask is not resolved into an allow.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_0
  - TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_1
-->
Start a detached self-hosted runner with the environment secret file ${TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_0.secret_file_path} (base dir ${TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_0.base_dir??TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_1})? The runner will execute that environment's queued sessions on this machine and will keep running after this session ends.
