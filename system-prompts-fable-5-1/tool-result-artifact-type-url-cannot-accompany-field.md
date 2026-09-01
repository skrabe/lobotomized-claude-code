<!--
name: Artifact type_url Cannot Accompany Field
description: >-
  validateInput rejection when url, pr_review, capabilities, contract, lang, or
  force accompanies type_url.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_TYPE_URL_CANNOT_ACCOMPANY_FIELD_VAR_0
-->
${TOOL_RESULT_ARTIFACT_TYPE_URL_CANNOT_ACCOMPANY_FIELD_VAR_0.length>1?`${TOOL_RESULT_ARTIFACT_TYPE_URL_CANNOT_ACCOMPANY_FIELD_VAR_0.slice(0,-1).join(", ")}${TOOL_RESULT_ARTIFACT_TYPE_URL_CANNOT_ACCOMPANY_FIELD_VAR_0.length>2?",":""} and ${TOOL_RESULT_ARTIFACT_TYPE_URL_CANNOT_ACCOMPANY_FIELD_VAR_0.at(-1)}`:TOOL_RESULT_ARTIFACT_TYPE_URL_CANNOT_ACCOMPANY_FIELD_VAR_0[0]} can't accompany \`type_url\` — a publish with \`type_url\` always creates a new Artifact whose page and settings come from the type; remove ${TOOL_RESULT_ARTIFACT_TYPE_URL_CANNOT_ACCOMPANY_FIELD_VAR_0.length>1?"them":"it"} (to update an Artifact you already created, omit \`type_url\` and pass its \`url\`)
