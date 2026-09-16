<!--
name: 'Tool Result: Artifact design-system other cards db get'
description: >-
  Tells the agent how to read unattached design-system cards by collection and
  doc_id via the store get action.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_DESIGN_SYSTEM_OTHER_CARDS_DB_GET_VAR_0
  - TOOL_RESULT_ARTIFACT_DESIGN_SYSTEM_OTHER_CARDS_DB_GET_VAR_1
  - TOOL_RESULT_ARTIFACT_DESIGN_SYSTEM_OTHER_CARDS_DB_GET_VAR_2
  - TOOL_RESULT_ARTIFACT_DESIGN_SYSTEM_OTHER_CARDS_DB_GET_VAR_3
-->
Its other cards are not attached: read one when you need it with ${TOOL_RESULT_ARTIFACT_DESIGN_SYSTEM_OTHER_CARDS_DB_GET_VAR_0('action "read_db" and `db_op`: "get"',()=>`the ${TOOL_RESULT_ARTIFACT_DESIGN_SYSTEM_OTHER_CARDS_DB_GET_VAR_1} tool, action "get"`)}, \`url\`: ${TOOL_RESULT_ARTIFACT_DESIGN_SYSTEM_OTHER_CARDS_DB_GET_VAR_2(TOOL_RESULT_ARTIFACT_DESIGN_SYSTEM_OTHER_CARDS_DB_GET_VAR_3)}, and a \`collection\` and \`doc_id\`: "api" and "tokens.md" (palette, type, fonts); "ds" and "tokens" (exact token values); "ds" and "meta" (the system's record). Where the README's index is shown, read a card it names by the collection and doc id the index gives.
