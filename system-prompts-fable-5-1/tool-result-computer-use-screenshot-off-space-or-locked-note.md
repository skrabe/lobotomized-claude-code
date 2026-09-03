<!--
name: 'Tool Result: Computer Use Screenshot Off-Space Or Locked Note'
description: >-
  Note appended to an app_screenshot result when the window is off-Space or the
  screen is locked.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_SCREENSHOT_OFF_SPACE_OR_LOCKED_NOTE_VAR_0
-->
these look the same from here. If it's just off-Space: for most apps this frame is current and you can still click/type into it in the background; for apps that only accept input when brought to the front (which would flash on-screen), the frame may be STALE and actions will be refused. If the screen is locked, actions are refused until it's unlocked. When an action here refuses because the window is off-Space, ${TOOL_RESULT_COMPUTER_USE_SCREENSHOT_OFF_SPACE_OR_LOCKED_NOTE_VAR_0}.

