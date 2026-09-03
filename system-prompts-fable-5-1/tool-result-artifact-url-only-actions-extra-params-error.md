<!--
name: Artifact URL-Only Actions Extra-Params Error
description: >-
  validateInput rejection when watch, unwatch, status, resume_replies,
  read_page_data, or verify is passed extra fields.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_URL_ONLY_ACTIONS_EXTRA_PARAMS_ERROR_VAR_0
  - TOOL_RESULT_ARTIFACT_URL_ONLY_ACTIONS_EXTRA_PARAMS_ERROR_VAR_1
  - TOOL_RESULT_ARTIFACT_URL_ONLY_ACTIONS_EXTRA_PARAMS_ERROR_VAR_2
-->
action "${TOOL_RESULT_ARTIFACT_URL_ONLY_ACTIONS_EXTRA_PARAMS_ERROR_VAR_0}" takes only ${TOOL_RESULT_ARTIFACT_URL_ONLY_ACTIONS_EXTRA_PARAMS_ERROR_VAR_0==="read_page_data"?"`url` and `schema`":TOOL_RESULT_ARTIFACT_URL_ONLY_ACTIONS_EXTRA_PARAMS_ERROR_VAR_1?"`url` (and `path`)":"`url`"} — remove ${TOOL_RESULT_ARTIFACT_URL_ONLY_ACTIONS_EXTRA_PARAMS_ERROR_VAR_2.join(", ")}.
