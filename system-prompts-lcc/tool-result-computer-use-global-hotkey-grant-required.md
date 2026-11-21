<!--
name: 'Tool result: global hotkey grant required'
description: >-
  Refusal explaining the chord may be a system-wide shortcut held by another
  program and asking for systemKeyCombos.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_GLOBAL_HOTKEY_GRANT_REQUIRED_VAR_0
-->
Another program may hold "${TOOL_RESULT_COMPUTER_USE_GLOBAL_HOTKEY_GRANT_REQUIRED_VAR_0}" as a system-wide shortcut, so pressing it could start something outside the apps you were granted. An Alt, Ctrl or Shift key that is already down counts toward this combination, so it may work once that key is released. Request the \`systemKeyCombos\` grant via request_access
