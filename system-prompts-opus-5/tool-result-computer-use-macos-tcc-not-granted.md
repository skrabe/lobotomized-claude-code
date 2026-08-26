<!--
name: 'Tool Result: Computer Use macOS TCC Not Granted'
description: >-
  request_access error when the user saw the macOS permission prompt but
  Accessibility/Screen Recording are still missing.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_MACOS_TCC_NOT_GRANTED_VAR_0
-->
The user saw the permission prompt but macOS ${TOOL_RESULT_COMPUTER_USE_MACOS_TCC_NOT_GRANTED_VAR_0.join(" and ")} permission(s) are still not granted. Do not retry in this turn. Let the user know these permissions need to be granted in the Claude desktop app on the computer where it's running. If the user grants them and sends a new request, you may call request_access again.
