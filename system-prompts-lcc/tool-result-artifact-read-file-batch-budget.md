<!--
name: 'Tool Result: Artifact Read File Batch Budget'
description: >-
  read_file batch error: earlier files in this call already hold the per-call MB
  cap, so later paths need another call.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_READ_FILE_BATCH_BUDGET_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_FILE_BATCH_BUDGET_VAR_1
-->
not fetched: the files read before it in this call already hold ${TOOL_RESULT_ARTIFACT_READ_FILE_BATCH_BUDGET_VAR_0.floor(TOOL_RESULT_ARTIFACT_READ_FILE_BATCH_BUDGET_VAR_1/1048576)}MB, the most one read carries — read it, and any after it, in another call
