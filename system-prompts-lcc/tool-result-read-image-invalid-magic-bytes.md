<!--
name: 'Tool result: image file content invalid'
description: >-
  Read tool error when a file with an image extension does not contain valid
  PNG/JPEG/GIF/WebP data
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_READ_IMAGE_INVALID_MAGIC_BYTES_VAR_0
  - TOOL_RESULT_READ_IMAGE_INVALID_MAGIC_BYTES_VAR_1
  - TOOL_RESULT_READ_IMAGE_INVALID_MAGIC_BYTES_VAR_2
  - TOOL_RESULT_READ_IMAGE_INVALID_MAGIC_BYTES_VAR_3
-->
File has an image extension but its content is not a valid PNG/JPEG/GIF/WebP. Detected: ${TOOL_RESULT_READ_IMAGE_INVALID_MAGIC_BYTES_VAR_0(TOOL_RESULT_READ_IMAGE_INVALID_MAGIC_BYTES_VAR_1)}. This usually means a download saved an error/login page instead of the image. Use \`file "${TOOL_RESULT_READ_IMAGE_INVALID_MAGIC_BYTES_VAR_2}"\` to confirm, or read it as text with ${TOOL_RESULT_READ_IMAGE_INVALID_MAGIC_BYTES_VAR_3} (e.g. \`head -c 500\`).
