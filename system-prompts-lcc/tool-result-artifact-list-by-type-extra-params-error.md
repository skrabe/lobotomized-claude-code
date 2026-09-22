<!--
name: Artifact List-By-Type Extra-Params Error
description: >-
  validateInput rejection when action list with type or type_url is passed
  fields other than scope and limit.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_EXTRA_PARAMS_ERROR_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_EXTRA_PARAMS_ERROR_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_EXTRA_PARAMS_ERROR_VAR_2
-->
action "list" with \`type\` or \`type_url\` takes only \`scope\` and \`limit\` — remove ${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_EXTRA_PARAMS_ERROR_VAR_0.join(", ")}.${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_EXTRA_PARAMS_ERROR_VAR_1().frozenArtifactTypes?.TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_EXTRA_PARAMS_ERROR_VAR_2===!0?" To start a new Artifact from the type, omit `action` and pass its `type_url`.":""}
