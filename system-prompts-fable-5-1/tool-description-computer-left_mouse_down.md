<!--
name: 'Tool Description: Computer left_mouse_down'
description: >-
  Describes the computer-use left_mouse_down tool for holding the left mouse
  button at the current cursor position
ccVersion: 2.1.246
variables:
  - FRONTMOST_APPLICATION_ALLOWLIST_GUARD
-->
Press the left mouse button at the current cursor position and leave it held. ${FRONTMOST_APPLICATION_ALLOWLIST_GUARD} Use mouse_move first to position the cursor. Call left_mouse_up to release. Errors if the button is already held.
