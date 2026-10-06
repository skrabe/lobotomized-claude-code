<!--
name: 'Tool Result: Write verification size mismatch'
description: >-
  Error returned when a file written by Write/Edit/NotebookEdit has a different
  on-disk size than expected, suggesting silent truncation.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WRITE_VERIFICATION_SIZE_MISMATCH_VAR_0
  - TOOL_RESULT_WRITE_VERIFICATION_SIZE_MISMATCH_VAR_1
  - TOOL_RESULT_WRITE_VERIFICATION_SIZE_MISMATCH_VAR_2
-->
Write verification failed: ${TOOL_RESULT_WRITE_VERIFICATION_SIZE_MISMATCH_VAR_0} is ${TOOL_RESULT_WRITE_VERIFICATION_SIZE_MISMATCH_VAR_1.size} bytes on disk, expected ${TOOL_RESULT_WRITE_VERIFICATION_SIZE_MISMATCH_VAR_2}. The filesystem may have silently truncated the write (network drive / cloud sync).
