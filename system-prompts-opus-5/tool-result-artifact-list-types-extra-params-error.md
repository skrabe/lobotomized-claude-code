<!--
name: Artifact list_types Extra-Params Error
description: >-
  validateInput rejection when list_types is passed fields other than
  type_query.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_2
-->
action "list_types" takes only \`type_query\` — remove ${TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_0.join(", ")}.${TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_1().frozenArtifactTypes?.TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_2===!0?" To start a new Artifact from a type, omit `action` and pass its `type_url`.":""}
