<!--
name: 'Tool result: app drag on pop-up menu refused'
description: >-
  Refusal that a drag cannot start on a pop-up menu in the background; start it
  beside the control.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_DRAG_ON_POPUP_MENU_REFUSED_VAR_0
-->
The drag starts on a pop-up menu (a dropdown). A press on it opens its menu, and in the background that menu takes the keyboard from the app the user is working in, so the drag was NOT sent. A drag cannot start on a pop-up menu: start it beside the control. To choose one of its options there is no dependable way in the background that leaves the user's keyboard alone. ${TOOL_RESULT_APP_DRAG_ON_POPUP_MENU_REFUSED_VAR_0}
