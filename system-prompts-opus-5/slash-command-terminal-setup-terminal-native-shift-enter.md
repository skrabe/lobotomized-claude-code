<!--
name: 'Slash Command: /terminal-setup — this terminal supports Shift+Enter natively'
description: >-
  Output telling the model the named terminal
  (Ghostty/Kitty/Warp/WezTerm/Windows Terminal) supports Shift+Enter natively
  and needs no configuration.
ccVersion: 2.1.235
variables:
  - SLASH_COMMAND_TERMINAL_SETUP_TERMINAL_NATIVE_SHIFT_ENTER_VAR_0
  - SLASH_COMMAND_TERMINAL_SETUP_TERMINAL_NATIVE_SHIFT_ENTER_VAR_1
-->
Shift+Enter is natively supported in ${SLASH_COMMAND_TERMINAL_SETUP_TERMINAL_NATIVE_SHIFT_ENTER_VAR_0[K.terminal]}.

No configuration needed. Just use Shift+Enter to add newlines.${SLASH_COMMAND_TERMINAL_SETUP_TERMINAL_NATIVE_SHIFT_ENTER_VAR_1()}
