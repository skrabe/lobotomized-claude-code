<!--
name: 'Tool Result: Artifact read version extra params'
description: 'Validation error: read with version takes only url, remove prompt/page'
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_ARTIFACT_READ_VERSION_EXTRA_PARAMS_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_VERSION_EXTRA_PARAMS_VAR_1
-->
action "read" with \`version\` saves that version to a file and takes only \`url\` besides — remove ${TOOL_RESULT_ARTIFACT_READ_VERSION_EXTRA_PARAMS_VAR_0.map((TOOL_RESULT_ARTIFACT_READ_VERSION_EXTRA_PARAMS_VAR_1)=>`\`${TOOL_RESULT_ARTIFACT_READ_VERSION_EXTRA_PARAMS_VAR_1}\``).join(" and ")}.
