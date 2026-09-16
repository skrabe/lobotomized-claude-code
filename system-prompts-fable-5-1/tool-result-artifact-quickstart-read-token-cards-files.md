<!--
name: 'Tool Result: Quickstart Read Token Cards (Files)'
description: >-
  Files-backed branch telling the model to read the design system's token cards
  via read/read_file paths in the same message.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_FILES_VAR_0
  - TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_FILES_VAR_1
  - TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_FILES_VAR_2
-->
 In the same message, read that design system's token cards — ${TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_FILES_VAR_0('action "read_file"',()=>'action "read"')}, \`url\`: ${TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_FILES_VAR_1}, once with \`path\`: "${TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_FILES_VAR_2}api/tokens.md" and once with \`path\`: "${TOOL_RESULT_ARTIFACT_QUICKSTART_READ_TOKEN_CARDS_FILES_VAR_2}tokens.json" — since the type's instructions will ask for them.
