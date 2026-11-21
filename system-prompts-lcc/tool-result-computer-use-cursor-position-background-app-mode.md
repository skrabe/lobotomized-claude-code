<!--
name: 'Tool Result: Computer Use Cursor Position Background App Mode'
description: >-
  cursor_position result note in background app-mode: x/y is where your last
  app_* action landed in app_screenshot coordinates; the live cursor is only
  reported under full-screen control.
ccVersion: 2.1.330
-->
background app-mode: x/y is where your own last app_* action landed, in that window's app_screenshot coordinates (null: no click or typing at a point yet). The user's live cursor is not reported in this mode, only under full-screen control (request_full_control) while holding no app windows.
