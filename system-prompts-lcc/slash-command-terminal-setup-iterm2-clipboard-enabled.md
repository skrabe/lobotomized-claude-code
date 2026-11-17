<!--
name: 'Slash Command: /terminal-setup iTerm2 clipboard enabled'
description: >-
  /terminal-setup output after turning on iTerm2's 'Applications in terminal may
  access clipboard', with restart and undo instructions.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_TERMINAL_SETUP_ITERM2_CLIPBOARD_ENABLED_VAR_0
  - SLASH_COMMAND_TERMINAL_SETUP_ITERM2_CLIPBOARD_ENABLED_VAR_1
  - SLASH_COMMAND_TERMINAL_SETUP_ITERM2_CLIPBOARD_ENABLED_VAR_2
  - SLASH_COMMAND_TERMINAL_SETUP_ITERM2_CLIPBOARD_ENABLED_VAR_3
-->
${SLASH_COMMAND_TERMINAL_SETUP_ITERM2_CLIPBOARD_ENABLED_VAR_0("success",SLASH_COMMAND_TERMINAL_SETUP_ITERM2_CLIPBOARD_ENABLED_VAR_1)('Turned on "Applications in terminal may access clipboard" in iTerm2')}${SLASH_COMMAND_TERMINAL_SETUP_ITERM2_CLIPBOARD_ENABLED_VAR_2}${SLASH_COMMAND_TERMINAL_SETUP_ITERM2_CLIPBOARD_ENABLED_VAR_3.dim("Restart iTerm2 for this to take effect. Undo: defaults write com.googlecode.iterm2 AllowClipboardAccess -bool false")}${SLASH_COMMAND_TERMINAL_SETUP_ITERM2_CLIPBOARD_ENABLED_VAR_2}${SLASH_COMMAND_TERMINAL_SETUP_ITERM2_CLIPBOARD_ENABLED_VAR_2}
