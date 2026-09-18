<!--
name: 'Tool Result: Coordinator Bash Read-Only Only'
description: >-
  Coordinator Bash refusal telling the model only a verifiable read-only
  in-workdir command is allowed here and anything else must run from a worker.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_BASH_COORDINATOR_READONLY_ONLY_VAR_0
  - TOOL_RESULT_BASH_COORDINATOR_READONLY_ONLY_VAR_1
-->
${TOOL_RESULT_BASH_COORDINATOR_READONLY_ONLY_VAR_0} in the coordinator runs only a command it can verify as read-only and that stays in the working directory (no cd, pushd or popd), with no input besides command, description and timeout (no run_in_background, no sandbox bypass, no other machine) — run anything else from a worker via the ${TOOL_RESULT_BASH_COORDINATOR_READONLY_ONLY_VAR_1} tool.
