<!--
name: 'Send to Project: Field byte limit'
description: >-
  Zod refine message for proposal string fields that exceed their byte limit,
  surfaced in send-to-project input validation.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_FIELD_MAX_BYTES_VAR_0
-->
must be at most ${TOOL_RESULT_SEND_TO_PROJECT_FIELD_MAX_BYTES_VAR_0} bytes
