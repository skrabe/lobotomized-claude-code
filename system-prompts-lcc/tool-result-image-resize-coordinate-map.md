<!--
name: Image resize coordinate-mapping annotation
description: >-
  Text annotation attached to a resized image block sent to the model, giving
  original/display sizes and a coordinate scale factor for computer-use.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_IMAGE_RESIZE_COORDINATE_MAP_VAR_0
  - TOOL_RESULT_IMAGE_RESIZE_COORDINATE_MAP_VAR_1
  - TOOL_RESULT_IMAGE_RESIZE_COORDINATE_MAP_VAR_2
  - TOOL_RESULT_IMAGE_RESIZE_COORDINATE_MAP_VAR_3
  - TOOL_RESULT_IMAGE_RESIZE_COORDINATE_MAP_VAR_4
-->
original ${TOOL_RESULT_IMAGE_RESIZE_COORDINATE_MAP_VAR_0}x${TOOL_RESULT_IMAGE_RESIZE_COORDINATE_MAP_VAR_1}, displayed at ${TOOL_RESULT_IMAGE_RESIZE_COORDINATE_MAP_VAR_2}x${TOOL_RESULT_IMAGE_RESIZE_COORDINATE_MAP_VAR_3}. Multiply coordinates by ${TOOL_RESULT_IMAGE_RESIZE_COORDINATE_MAP_VAR_4.toFixed(2)} to map to original image.
