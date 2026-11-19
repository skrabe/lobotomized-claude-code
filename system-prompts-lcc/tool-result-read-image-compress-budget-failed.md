<!--
name: 'Read image: could not compress under budget'
description: >-
  Read tool error when an image cannot be compressed under the target raw size;
  tells the model to resize or use a smaller image.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_READ_IMAGE_COMPRESS_BUDGET_FAILED_VAR_0
  - TOOL_RESULT_READ_IMAGE_COMPRESS_BUDGET_FAILED_VAR_1
  - TOOL_RESULT_READ_IMAGE_COMPRESS_BUDGET_FAILED_VAR_2
  - TOOL_RESULT_READ_IMAGE_COMPRESS_BUDGET_FAILED_VAR_3
-->
Unable to compress image (${TOOL_RESULT_READ_IMAGE_COMPRESS_BUDGET_FAILED_VAR_0(TOOL_RESULT_READ_IMAGE_COMPRESS_BUDGET_FAILED_VAR_1)}) to under ${TOOL_RESULT_READ_IMAGE_COMPRESS_BUDGET_FAILED_VAR_2.floor(TOOL_RESULT_READ_IMAGE_COMPRESS_BUDGET_FAILED_VAR_3.targetRawSize/1024/1024*10)/10}MB. Resize it or use a smaller image.
