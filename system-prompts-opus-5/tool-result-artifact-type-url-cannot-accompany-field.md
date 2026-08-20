<!--
name: 'Tool Result: type_url Cannot Accompany Field'
description: >-
  validateInput rejection when a publish with type_url also sets url, pr_review,
  capabilities, contract, lang, or force.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_TYPE_URL_CANNOT_ACCOMPANY_FIELD_VAR_0
-->
\`${TOOL_RESULT_ARTIFACT_TYPE_URL_CANNOT_ACCOMPANY_FIELD_VAR_0}\` can't accompany \`type_url\` — a publish with \`type_url\` always creates a new Artifact whose page and settings come from the type; remove \`${TOOL_RESULT_ARTIFACT_TYPE_URL_CANNOT_ACCOMPANY_FIELD_VAR_0}\` (to update an Artifact you already created, omit \`type_url\` and pass its \`url\`)
