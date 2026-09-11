<!--
name: Artifact Read Run Script Mutation Fill
description: >-
  Created-from-type fill guidance: no store-write tool, but run_script mutation
  can write because the type declares endpoints.
ccVersion: 2.1.268
variables:
  - TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_1
  - TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_2
-->
${TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_0}, and no store-write call is served here — the type declares endpoints, so the ${TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_1} tool's \`action: "run_script"\` with \`mode: "mutation"\` can write it (\`get_endpoints\` first); ${TOOL_RESULT_ARTIFACT_READ_RUN_SCRIPT_MUTATION_FILL_VAR_2}
