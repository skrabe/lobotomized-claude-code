<!--
name: Artifact URL-Only Actions Extra-Params Error
description: >-
  validateInput rejection when a URL-only Artifact action (watch, unwatch,
  status, verify, ...) is passed extra fields.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_ARTIFACT_URL_ONLY_ACTIONS_EXTRA_PARAMS_ERROR_VAR_0
  - TOOL_RESULT_ARTIFACT_URL_ONLY_ACTIONS_EXTRA_PARAMS_ERROR_VAR_1
-->
action "${TOOL_RESULT_ARTIFACT_URL_ONLY_ACTIONS_EXTRA_PARAMS_ERROR_VAR_0}" takes only \`url\` — remove ${TOOL_RESULT_ARTIFACT_URL_ONLY_ACTIONS_EXTRA_PARAMS_ERROR_VAR_1.join(", ")}.
