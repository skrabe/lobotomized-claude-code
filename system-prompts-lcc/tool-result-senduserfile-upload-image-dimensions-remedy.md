<!--
name: 'Tool Result: SendUserFile Upload Image Dimensions Remedy'
description: >-
  Remedy appended to a SendUserFile upload error when an image is too wide or
  tall: send a copy scaled to at most the pixel limit, or a non-image format
  such as a .zip.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_SENDUSERFILE_UPLOAD_IMAGE_DIMENSIONS_REMEDY_VAR_0
-->
send a copy scaled to at most ${TOOL_RESULT_SENDUSERFILE_UPLOAD_IMAGE_DIMENSIONS_REMEDY_VAR_0} pixels on its longer side, or send it in a non-image format such as a .zip
