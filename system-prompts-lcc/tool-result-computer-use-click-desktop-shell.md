<!--
name: 'Tool Result: Computer-Use Click Desktop Shell'
description: >-
  Hit-test tool result when a click would land on the desktop shell rather than
  an allowed app.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_CLICK_DESKTOP_SHELL_VAR_0
-->
The click would land on the desktop shell (Dock, Spotlight, desktop icons, or the taskbar/Start menu). These can launch applications outside the allowlist. To interact with any of them, call request_access with exactly "${TOOL_RESULT_COMPUTER_USE_CLICK_DESKTOP_SHELL_VAR_0}" in the 
