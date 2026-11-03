<!--
name: 'Tool Result: Email file reference checksum mismatch'
description: >-
  Says a referenced file doesn't match its SHA-256 so nothing was sent, asking
  to recompute and retry
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_CHECKSUM_MISMATCH_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_CHECKSUM_MISMATCH_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_CHECKSUM_MISMATCH_VAR_2
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_CHECKSUM_MISMATCH_VAR_0} doesn't match the SHA-256 in its reference, ${TOOL_RESULT_EMAIL_FILE_REFERENCE_CHECKSUM_MISMATCH_VAR_1} Compute its SHA-256 again (${TOOL_RESULT_EMAIL_FILE_REFERENCE_CHECKSUM_MISMATCH_VAR_2()}) and make the call again. A SHA-256 that wasn't computed from the file won't match.
