<!--
name: Artifact list_types Extra-Params Error
description: >-
  validateInput rejection when list_types is passed fields other than
  type_query.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_2
  - TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_3
-->
action "list_types" takes ${TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_0?.TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_1===!0?"only `type_query`":"no other fields"} — remove ${TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_2.join(", ")}.${TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_0?.TOOL_RESULT_ARTIFACT_LIST_TYPES_EXTRA_PARAMS_ERROR_VAR_3===!0?" To start a new Artifact from a type, omit `action` and pass its `type_url`.":""}
