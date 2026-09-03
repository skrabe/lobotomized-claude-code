<!--
name: Computer-use App Right-Click Context Menu Refused
description: >-
  app_click tool_result refusing a right-click because opening a context menu
  would bring the app to the front.
ccVersion: 2.1.246
-->
Opening a context (right-click) menu would bring the app to the front, so it was NOT done. Use app_menu to run the equivalent menu bar command, or click the target directly. To use the context menu itself, call app_release and use the display-scope tools.
