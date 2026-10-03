<!--
name: 'Tool Result: Attachment Scaled Image Size Row'
description: >-
  Per-image row listing the sent pixel size, the original size and whether the
  original is in the project folder or unchanged on disk.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_ATTACHMENT_SCALED_IMAGE_SIZE_ROW_VAR_0
  - TOOL_RESULT_ATTACHMENT_SCALED_IMAGE_SIZE_ROW_VAR_1
  - TOOL_RESULT_ATTACHMENT_SCALED_IMAGE_SIZE_ROW_VAR_2
-->
  ${TOOL_RESULT_ATTACHMENT_SCALED_IMAGE_SIZE_ROW_VAR_0}: sent at ${TOOL_RESULT_ATTACHMENT_SCALED_IMAGE_SIZE_ROW_VAR_1.width}×${TOOL_RESULT_ATTACHMENT_SCALED_IMAGE_SIZE_ROW_VAR_1.height} pixels; the original (${TOOL_RESULT_ATTACHMENT_SCALED_IMAGE_SIZE_ROW_VAR_1.original_width}×${TOOL_RESULT_ATTACHMENT_SCALED_IMAGE_SIZE_ROW_VAR_1.original_height}) is ${TOOL_RESULT_ATTACHMENT_SCALED_IMAGE_SIZE_ROW_VAR_2?"in the project folder":"unchanged on disk"}
