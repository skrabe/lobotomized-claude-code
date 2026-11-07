<!--
name: 'Tool Result: write verification bytes differ'
description: >-
  Error when the bytes read back after a write differ from what was written,
  suggesting a partial write or another process changing the file
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WRITE_VERIFICATION_BYTES_DIFFER_VAR_0
-->
Write verification failed: ${TOOL_RESULT_WRITE_VERIFICATION_BYTES_DIFFER_VAR_0} does not hold what was written. The filesystem may have silently kept only part of the write, or another process may have changed the file.
