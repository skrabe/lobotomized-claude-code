<!--
name: Computer-use App Replaced Previous Content
description: >-
  Success-result note that previous field content was replaced and how to
  restore it with app_type.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_APP_REPLACED_PREVIOUS_CONTENT_VAR_0
  - TOOL_RESULT_COMPUTER_USE_APP_REPLACED_PREVIOUS_CONTENT_VAR_1
  - TOOL_RESULT_COMPUTER_USE_APP_REPLACED_PREVIOUS_CONTENT_VAR_2
-->
 Replaced previous content (${TOOL_RESULT_COMPUTER_USE_APP_REPLACED_PREVIOUS_CONTENT_VAR_0.previousContentTruncated?"TRUNCATED — original was longer than 500 chars; ":""}restore by app_type with overwrite_existing: true${TOOL_RESULT_COMPUTER_USE_APP_REPLACED_PREVIOUS_CONTENT_VAR_1==="focused"?' and target: "focused" again (a bare retry would aim at the last pointed coordinate instead)':""} and this text): ${TOOL_RESULT_COMPUTER_USE_APP_REPLACED_PREVIOUS_CONTENT_VAR_2(TOOL_RESULT_COMPUTER_USE_APP_REPLACED_PREVIOUS_CONTENT_VAR_0.previousContent)}.
