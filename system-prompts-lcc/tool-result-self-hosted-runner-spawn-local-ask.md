<!--
name: 'Self-Hosted Runner: Spawn Local Runner Ask'
description: >-
  Permission-request text for starting a detached self-hosted runner on this
  machine; becomes the tool_result the model reads if the user rejects.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_0
  - TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_1
  - TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_2
  - TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_3
-->
Start a detached self-hosted runner with the environment secret file ${TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_0(TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_1.secret_file_path)} (base dir ${TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_0(TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_1.base_dir??TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_2)}, log ${TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_0(TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_1.log_path??TOOL_RESULT_SELF_HOSTED_RUNNER_SPAWN_LOCAL_ASK_VAR_3)})? The runner will execute that environment's queued sessions on this machine and will keep running after this session ends.
