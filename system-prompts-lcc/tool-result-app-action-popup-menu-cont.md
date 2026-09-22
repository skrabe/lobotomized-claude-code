<!--
name: 'Tool Result: App Action Popup Menu Continued'
description: >-
  Continuation of the popup_menu reason: the click was not performed; use
  app_menu or display-scope tools.
ccVersion: 2.1.246
-->
the front, and the app_* tools can't select a menu option in the background, so it was NOT clicked. If the same command exists in the menu bar, use app_menu instead; otherwise call app_release and use the display-scope tools (which take over the screen), or ask the user
