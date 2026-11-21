<!--
name: 'Tool result: app GTK background drag refused'
description: >-
  Refusal that GTK apps ignore background drags, suggesting menu, keys or typing
  instead.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_GTK_BACKGROUND_DRAG_REFUSED_VAR_0
  - TOOL_RESULT_APP_GTK_BACKGROUND_DRAG_REFUSED_VAR_1
  - TOOL_RESULT_APP_GTK_BACKGROUND_DRAG_REFUSED_VAR_2
-->
${TOOL_RESULT_APP_GTK_BACKGROUND_DRAG_REFUSED_VAR_0(TOOL_RESULT_APP_GTK_BACKGROUND_DRAG_REFUSED_VAR_1)} is built on GTK, which ignores drags sent to it in the background (only the press would register), so the drag was NOT sent. Look for another way first: a menu command, a keyboard shortcut, or typing the value into the app's own input fields (app_menu, app_key, app_type). ${TOOL_RESULT_APP_GTK_BACKGROUND_DRAG_REFUSED_VAR_2}
