<!--
name: Artifact Read Extra-Params Error
description: >-
  validateInput rejection when action read is passed fields other than url,
  prompt, and optionally page.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_READ_EXTRA_PARAMS_ERROR_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_EXTRA_PARAMS_ERROR_VAR_1
-->
action "read" takes only \`url\`${TOOL_RESULT_ARTIFACT_READ_EXTRA_PARAMS_ERROR_VAR_0?", `prompt` and `page`":" and `prompt`"} — remove ${TOOL_RESULT_ARTIFACT_READ_EXTRA_PARAMS_ERROR_VAR_1.join(", ")}.
