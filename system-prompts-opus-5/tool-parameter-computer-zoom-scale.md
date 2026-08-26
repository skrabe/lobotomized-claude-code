<!--
name: 'Tool Parameter: Computer zoom scale'
description: >-
  Zoom action scale param: smaller images use fewer tokens; region/click
  coordinates stay in the full-resolution frame.
ccVersion: 2.1.246
variables:
  - TOOL_PARAMETER_COMPUTER_ZOOM_SCALE_VAR_0
  - TOOL_PARAMETER_COMPUTER_ZOOM_SCALE_VAR_1
-->
Scale factor in [${TOOL_PARAMETER_COMPUTER_ZOOM_SCALE_VAR_0}, ${TOOL_PARAMETER_COMPUTER_ZOOM_SCALE_VAR_1}] for the returned zoom image; smaller images use fewer tokens. Region and click coordinates always stay in the full-resolution coordinate frame; never rescale coordinates yourself.
