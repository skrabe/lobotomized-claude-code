<!--
name: 'Tool result: app system drag session refused'
description: >-
  Refusal that a drag starting on a link or picture would start a system drag
  session and steal focus.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_SYSTEM_DRAG_SESSION_REFUSED_VAR_0
  - TOOL_RESULT_APP_SYSTEM_DRAG_SESSION_REFUSED_VAR_1
-->
The drag starts on a link or a picture, which ${TOOL_RESULT_APP_SYSTEM_DRAG_SESSION_REFUSED_VAR_0(TOOL_RESULT_APP_SYSTEM_DRAG_SESSION_REFUSED_VAR_1)} would pick up and drag as an item. In the background that takes keyboard focus from the app the user is working in, so the drag was NOT sent. Look for another way first: start the drag just beside the link or picture, or reach the same result with a click, a menu command or the keyboard (app_click, app_menu, app_key). 
