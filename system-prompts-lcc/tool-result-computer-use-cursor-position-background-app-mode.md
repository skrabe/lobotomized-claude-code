<!--
name: 'Tool Result: Computer Use Cursor Position Background App Mode'
description: >-
  Error tool result when cursor_position is requested while background app-mode
  holds the lock.
ccVersion: 2.1.246
-->
cursor_position reads the live host cursor and is not available in background app-mode. Use the last app_screenshot's coordinates instead.
