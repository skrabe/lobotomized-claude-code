<!--
name: 'Tool Result: PNG image over limit, compression failed'
description: >-
  Tells Claude an image exceeded the size limit and could not be compressed, and
  to resize it or use a smaller image
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_IMAGE_PNG_OVER_LIMIT_COMPRESSION_FAILED_VAR_0
  - TOOL_RESULT_IMAGE_PNG_OVER_LIMIT_COMPRESSION_FAILED_VAR_1
-->
it is over the ${TOOL_RESULT_IMAGE_PNG_OVER_LIMIT_COMPRESSION_FAILED_VAR_0.floor(TOOL_RESULT_IMAGE_PNG_OVER_LIMIT_COMPRESSION_FAILED_VAR_1.targetRawSize/1024/1024*10)/10}MB limit and compression failed. Resize it or use a smaller image.
