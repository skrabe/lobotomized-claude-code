<!--
name: 'App action: popup menu not clicked (Windows)'
description: >-
  Refusal: dropdown not clicked; use app_key up/down or tab; app_menu for menu
  bar.
ccVersion: 2.1.330
-->
this is a dropdown or menu control whose list opens as a popup over whatever the user is doing. It was NOT clicked, or its popup was closed again at once: nothing is open now. Do not retry it. For a dropdown, send app_key up or down with the dropdown's own coordinate, which changes the value without opening the list. If that does nothing, first move the keyboard focus onto it with app_key tab, checking with app_screenshot. Store/WinUI apps take no background keys. For a menu bar command use app_menu
