<!--
name: Artifact List Extra-Params Error
description: >-
  validateInput rejection when action list is passed fields other than limit and
  scope, with an optional type-catalog clause.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_LIST_EXTRA_PARAMS_ERROR_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_EXTRA_PARAMS_ERROR_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_EXTRA_PARAMS_ERROR_VAR_2
-->
action "list" takes only \`limit\` and \`scope\`${TOOL_RESULT_ARTIFACT_LIST_EXTRA_PARAMS_ERROR_VAR_0().frozenArtifactTypes?.TOOL_RESULT_ARTIFACT_LIST_EXTRA_PARAMS_ERROR_VAR_1===!0?" (or `type` or `type_url`, to list the Artifacts made from a type)":""} — remove ${TOOL_RESULT_ARTIFACT_LIST_EXTRA_PARAMS_ERROR_VAR_2.join(", ")}. To publish or update an artifact, omit \`action\`.
