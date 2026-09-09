<!--
name: Artifact Read Run Script Mutation Fill
description: >-
  Artifact-read fill guidance when only run_script mode mutation can write the
  store, after get_endpoints.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_1
  - TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_2
-->
${TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_0}, and no store-write call is served here — only if the type declares endpoints can the ${TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_1} tool's \`action: "run_script"\` with \`mode: "mutation"\` write it (\`get_endpoints\` first); ${TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_2}
