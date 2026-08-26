<!--
name: 'Tool Result: App Action Context Menu Refused'
description: >-
  Reason-mapper text when a right-click context menu was refused because opening
  it would bring the app to the front.
ccVersion: 2.1.246
-->
opening a context (right-click) menu would bring the app to the front, so it was NOT done. Use app_menu to run the equivalent menu bar command, or click the target directly. To use the context menu itself, call app_release and use the display-scope tools
