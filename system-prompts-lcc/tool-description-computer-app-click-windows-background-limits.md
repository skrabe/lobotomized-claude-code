<!--
name: 'Tool Description: app_click Windows background limits'
description: >-
  app_click Windows arm: what background control can do and which inputs need
  full control.
ccVersion: 2.1.330
-->
 On Windows, background control works through accessibility actions and window messages only: it can press buttons, toggle checkboxes, select list/tree/tab items, set the text of standard text fields, scroll, and pick menu-bar commands (app_menu). These need full control instead: keyboard shortcuts with Ctrl/Alt/Win, arrow/Tab/Enter navigation outside classic dialogs, typing into documents, rich-text editors and chat message boxes, drag, right-click, hover, and any click on a spot that is not a listed element in Chrome/Electron-based, WPF or Store apps.
