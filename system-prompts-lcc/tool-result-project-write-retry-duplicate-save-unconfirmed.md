<!--
name: Project write uncertain duplicate retry advice
description: >-
  Adds readback and limited retry advice when a replacement save may have
  created a duplicate.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_PROJECT_WRITE_RETRY_DUPLICATE_SAVE_UNCONFIRMED_VAR_0
  - TOOL_RESULT_PROJECT_WRITE_RETRY_DUPLICATE_SAVE_UNCONFIRMED_VAR_1
-->
 ${TOOL_RESULT_PROJECT_WRITE_RETRY_DUPLICATE_SAVE_UNCONFIRMED_VAR_0} ${TOOL_RESULT_PROJECT_WRITE_RETRY_DUPLICATE_SAVE_UNCONFIRMED_VAR_1} If that fails too, tell the user that the new content may not have been saved, and offer it to them another way.
