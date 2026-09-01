<!--
name: 'Slash Command: /terminal-setup — Zed Keymap Manual Block'
description: >-
  /terminal-setup dim helper showing the Zed keymap.json Shift+Enter binding to
  add by hand when the installer cannot write it.
ccVersion: 2.1.247
variables:
  - SLASH_COMMAND_TERMINAL_SETUP_ZED_KEYMAP_MANUAL_BLOCK_VAR_0
  - SLASH_COMMAND_TERMINAL_SETUP_ZED_KEYMAP_MANUAL_BLOCK_VAR_1
  - SLASH_COMMAND_TERMINAL_SETUP_ZED_KEYMAP_MANUAL_BLOCK_VAR_2
-->
To add the binding yourself, add this block to the keymap array in ${SLASH_COMMAND_TERMINAL_SETUP_ZED_KEYMAP_MANUAL_BLOCK_VAR_0(SLASH_COMMAND_TERMINAL_SETUP_ZED_KEYMAP_MANUAL_BLOCK_VAR_1)}:${SLASH_COMMAND_TERMINAL_SETUP_ZED_KEYMAP_MANUAL_BLOCK_VAR_2}{ "context": "Terminal", "bindings": { "shift-enter": ["terminal::SendText", "\\u001b\\r"] } }
