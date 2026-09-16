<!--
name: 'Tool Result: Quickstart Read Token Cards (Store)'
description: >-
  Store-backed branch telling the model to read the design system's token cards
  via read_db get in the same message.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_STORE_VAR_0
  - TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_STORE_VAR_1
  - TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_STORE_VAR_2
-->
 In the same message, read that design system's token cards — ${TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_STORE_VAR_0('action "read_db" with `db_op`: "get"',()=>`the ${TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_STORE_VAR_1} tool, action "get"`)}, \`url\`: ${TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_STORE_VAR_2}, once with \`collection\`: "api", \`doc_id\`: "tokens.md" and once with \`collection\`: "ds", \`doc_id\`: "tokens" — since the type's instructions will ask for them.
