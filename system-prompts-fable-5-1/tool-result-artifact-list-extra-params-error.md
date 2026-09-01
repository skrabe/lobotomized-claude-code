<!--
name: Artifact list extra-params error
description: >-
  Artifact validateInput error telling the model the list action takes only
  limit and scope, listing the extra keys to remove.
ccVersion: 2.1.210
variables:
  - TOOL_RESULT_ARTIFACT_LIST_EXTRA_PARAMS_ERROR_VAR_0
-->
action "list" takes only \`limit\` and \`scope\` — remove ${TOOL_RESULT_ARTIFACT_LIST_EXTRA_PARAMS_ERROR_VAR_0.join(", ")}. To publish or update an artifact, omit \`action\`.
