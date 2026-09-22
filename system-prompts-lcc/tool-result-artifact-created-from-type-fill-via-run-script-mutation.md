<!--
name: Artifact Created-From-Type Fill Via run_script Mutation
description: >-
  created_from_type tool_result when store-write is only available through
  run_script mode mutation endpoints.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_RUN_SCRIPT_MUTATION_VAR_0
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_RUN_SCRIPT_MUTATION_VAR_1
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_RUN_SCRIPT_MUTATION_VAR_2
-->
This type's instructions fill it through its own store, not with its page or data files, and no store-write call is served here. Only if the type declares endpoints (a handlers.js among the type's files above) can \`action: "run_script"\` with \`mode: "mutation"\` write that store through its db globals (\`get_endpoints\` first), passing \`url\`: ${TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_RUN_SCRIPT_MUTATION_VAR_0(TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_RUN_SCRIPT_MUTATION_VAR_1)}, as those instructions below describe (they cover only this Artifact's own content)${TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_RUN_SCRIPT_MUTATION_VAR_2}; otherwise it cannot be filled from here — tell the user that, and offer what those instructions suggest instead if they cover this case. Do not publish \`file_path\`/\`files\` to it as its content, and never index.html or any of the type's files.
