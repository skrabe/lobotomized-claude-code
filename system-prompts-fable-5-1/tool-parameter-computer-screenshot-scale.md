<!--
name: 'Tool Parameter: Computer screenshot scale'
description: >-
  Screenshot scale param: factor in [0.1, 1] for the returned image, with
  coordinates always in the full-resolution frame.
ccVersion: 2.1.246
variables:
  - TOOL_PARAMETER_COMPUTER_SCREENSHOT_SCALE_VAR_0
  - TOOL_PARAMETER_COMPUTER_SCREENSHOT_SCALE_VAR_1
-->
Scale factor in [${TOOL_PARAMETER_COMPUTER_SCREENSHOT_SCALE_VAR_0}, ${TOOL_PARAMETER_COMPUTER_SCREENSHOT_SCALE_VAR_1}] for the returned image; 1 (default) uses the full image token budget, 0.5 returns an image at half the width and height (~quarter of the tokens). Coordinates are ALWAYS in the full-resolution coordinate frame (reported with every scaled screenshot), never in the scaled image's own pixels.
