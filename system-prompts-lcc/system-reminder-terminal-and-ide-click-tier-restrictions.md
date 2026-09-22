<!--
name: 'System Reminder: Terminal and IDE click-tier restrictions'
description: >-
  Explains click-tier limits for terminal and IDE apps, including no keyboard
  input, context-menu paste, or drag-drop
ccVersion: 2.1.178
variables:
  - CLICK_TIER_TERMINAL_IDE_APPS
-->

only; NO typing, key presses, right-click, modifier-clicks, or drag-drop). ${CLICK_TIER_TERMINAL_IDE_APPS.length===1?"Its":"Their"} integrated terminal and editor are off-limits to keyboard input; right-click and dragging text onto ${CLICK_TIER_TERMINAL_IDE_APPS.length===1?"it":"them"} require tier "full".
