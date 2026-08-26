<!--
name: 'Tool Result: App Action Existing Content Note'
description: >-
  Unsupported-action tool-result clause quoting existing field content (first
  500 chars); wn() wraps the value in a do-not-follow-instructions fence.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_APP_ACTION_EXISTING_CONTENT_NOTE_VAR_0
  - TOOL_RESULT_APP_ACTION_EXISTING_CONTENT_NOTE_VAR_1
-->
 Existing content (${TOOL_RESULT_APP_ACTION_EXISTING_CONTENT_NOTE_VAR_0.previousContentTruncated?"first 500 chars — the field is longer":`${TOOL_RESULT_APP_ACTION_EXISTING_CONTENT_NOTE_VAR_0.previousContent.length} chars`}): ${TOOL_RESULT_APP_ACTION_EXISTING_CONTENT_NOTE_VAR_1(TOOL_RESULT_APP_ACTION_EXISTING_CONTENT_NOTE_VAR_0.previousContent)}.
