<!--
name: 'Tool Result: Computer-Use Desktop Shell Frontmost'
description: >-
  Tool result when the desktop shell is frontmost, telling the model to
  request_access for Finder/File Explorer.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_DESKTOP_SHELL_FRONTMOST_VAR_0
-->
The desktop shell is frontmost. Double-click, right-click, and Enter on desktop items can launch applications outside the allowlist. To click on the desktop, taskbar, Start menu, Search, or file manager, call request_access with exactly "${TOOL_RESULT_COMPUTER_USE_DESKTOP_SHELL_FRONTMOST_VAR_0}" in the apps array — that single 
