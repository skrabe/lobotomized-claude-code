<!--
name: 'Slash Command: /terminal-setup — iTerm2 already supports Shift+Enter'
description: >-
  Tells the model that no key-binding install happened because the host terminal
  is iTerm2, which handles Shift+Enter itself, so there is nothing left to
  configure.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_TERMINAL_SETUP_ITERM2_NATIVE_SHIFT_ENTER_VAR_0
  - SLASH_COMMAND_TERMINAL_SETUP_ITERM2_NATIVE_SHIFT_ENTER_VAR_1
  - SLASH_COMMAND_TERMINAL_SETUP_ITERM2_NATIVE_SHIFT_ENTER_VAR_2
-->
${await SLASH_COMMAND_TERMINAL_SETUP_ITERM2_NATIVE_SHIFT_ENTER_VAR_0(SLASH_COMMAND_TERMINAL_SETUP_ITERM2_NATIVE_SHIFT_ENTER_VAR_1.options.theme)}Shift+Enter is natively supported in iTerm2.

No configuration needed. Just use Shift+Enter to add newlines.${SLASH_COMMAND_TERMINAL_SETUP_ITERM2_NATIVE_SHIFT_ENTER_VAR_2()}
