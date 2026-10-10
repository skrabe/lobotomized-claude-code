<!--
name: 'Tool Result: Read too large, full-read option hint'
description: >-
  Suffix appended to the Read size/token limit error telling the model it may
  retry with the full-read option only when it genuinely needs the whole file.
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_READ_FILE_TOO_LARGE_FULL_READ_HINT_VAR_0
  - TOOL_RESULT_READ_FILE_TOO_LARGE_FULL_READ_HINT_VAR_1
-->
 To read it anyway, up to what still fits in your context, call ${TOOL_RESULT_READ_FILE_TOO_LARGE_FULL_READ_HINT_VAR_0} again with ${TOOL_RESULT_READ_FILE_TOO_LARGE_FULL_READ_HINT_VAR_1}: true — only if you genuinely need all of it or the user asked for the whole file.
