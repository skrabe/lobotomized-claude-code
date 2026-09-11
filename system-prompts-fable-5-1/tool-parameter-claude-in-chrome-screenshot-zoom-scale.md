<!--
name: 'Tool Parameter: Claude in Chrome Screenshot Zoom Scale'
description: >-
  Documents the scale factor for screenshot and zoom actions on the Claude in
  Chrome computer tool, including the full-resolution coordinate frame and
  extension-version requirement.
ccVersion: 2.1.268
variables:
  - TOOL_PARAMETER_CLAUDE_IN_CHROME_SCREENSHOT_ZOOM_SCALE_VAR_0
  - TOOL_PARAMETER_CLAUDE_IN_CHROME_SCREENSHOT_ZOOM_SCALE_VAR_1
-->
For \`screenshot\` and \`zoom\` only. Scale factor in [${TOOL_PARAMETER_CLAUDE_IN_CHROME_SCREENSHOT_ZOOM_SCALE_VAR_0}, ${TOOL_PARAMETER_CLAUDE_IN_CHROME_SCREENSHOT_ZOOM_SCALE_VAR_1}] for the returned image; 1 (default) uses the full image token budget, 0.5 returns an image at half the width and height (~quarter of the tokens). Coordinates are ALWAYS in the full-resolution coordinate frame (reported with every scaled screenshot), never in the scaled image's own pixels. Requires a Claude in Chrome extension version that supports scale; older extensions return the full-size image.
