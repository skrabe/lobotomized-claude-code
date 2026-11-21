<!--
name: 'Tool description: computer cursor_position background mode'
description: >-
  Suffix of cursor_position description (appScoped darwin) explaining
  background-mode reporting in app_screenshot coordinates.
ccVersion: 2.1.330
-->
 In background mode it instead returns one point: where your own last app_* action landed, in that window's app_screenshot coordinates. You are in background mode while you hold app windows. Until this session has full-screen control (request_full_control, unless full control is already its default) you are also in background mode while you still have windows captured with app_screenshot that you have not released, and whenever this session works in the background by default (the access request's result says which). Otherwise the user's live cursor is reported, and when it is over a window you captured with app_screenshot the result also includes appWindow: the same position in that window's app_screenshot coordinates.
