<!--
name: Artifact describe_type Extra-Params Error
description: >-
  validateInput rejection when describe_type is passed fields other than
  type_url.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_EXTRA_PARAMS_ERROR_VAR_0
  - TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_EXTRA_PARAMS_ERROR_VAR_1
  - TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_EXTRA_PARAMS_ERROR_VAR_2
-->
action "describe_type" takes only \`type_url\` — remove ${TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_EXTRA_PARAMS_ERROR_VAR_0.join(", ")}.${TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_EXTRA_PARAMS_ERROR_VAR_1().frozenArtifactTypes?.TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_EXTRA_PARAMS_ERROR_VAR_2===!0?" To start a new Artifact from the type, omit `action`.":""}
