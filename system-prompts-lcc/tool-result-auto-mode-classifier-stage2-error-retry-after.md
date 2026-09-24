<!--
name: 'Tool Result: Auto mode classifier stage 2 error with retry-after'
description: >-
  Auto-mode classifier block reason for a stage 2 error where the API gave a
  retry-after. It says the block is based on the stage 1 assessment and tells
  the model not to retry before the given time.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_STAGE2_ERROR_RETRY_AFTER_VAR_0
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_STAGE2_ERROR_RETRY_AFTER_VAR_1
-->
Stage 2 classifier error - blocking based on stage 1 assessment (the API told the classifier to wait ${TOOL_RESULT_AUTO_MODE_CLASSIFIER_STAGE2_ERROR_RETRY_AFTER_VAR_0(TOOL_RESULT_AUTO_MODE_CLASSIFIER_STAGE2_ERROR_RETRY_AFTER_VAR_1)} from now, so do not retry before then)
