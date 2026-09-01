<!--
name: 'Slash Command: /terminal-setup — cannot run from this terminal'
description: >-
  Tells the model the shortcut install was refused because of where it is
  running, and gives the workaround (backslash+return works now; re-run outside
  tmux/screen in a listed terminal), so the model does not report success or
  retry blindly.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_TERMINAL_SETUP_CANNOT_RUN_FROM_TERMINAL_VAR_0
  - SLASH_COMMAND_TERMINAL_SETUP_CANNOT_RUN_FROM_TERMINAL_VAR_1
  - SLASH_COMMAND_TERMINAL_SETUP_CANNOT_RUN_FROM_TERMINAL_VAR_2
  - SLASH_COMMAND_TERMINAL_SETUP_CANNOT_RUN_FROM_TERMINAL_VAR_3
  - SLASH_COMMAND_TERMINAL_SETUP_CANNOT_RUN_FROM_TERMINAL_VAR_4
-->
Terminal setup cannot be run from ${SLASH_COMMAND_TERMINAL_SETUP_CANNOT_RUN_FROM_TERMINAL_VAR_0}.

This command configures a convenient Shift+Enter shortcut for multi-line prompts.
${SLASH_COMMAND_TERMINAL_SETUP_CANNOT_RUN_FROM_TERMINAL_VAR_1.dim("Note: You can already use backslash (\\\\) + return to add newlines.")}

To set up the shortcut (optional):
1. Exit tmux/screen temporarily
2. Run /terminal-setup directly in one of these terminals:
${SLASH_COMMAND_TERMINAL_SETUP_CANNOT_RUN_FROM_TERMINAL_VAR_2}   • IDE: VSCode, Cursor, Devin Desktop, Zed
   • Other: Alacritty
3. Return to tmux/screen - settings will persist

${SLASH_COMMAND_TERMINAL_SETUP_CANNOT_RUN_FROM_TERMINAL_VAR_1.dim("Note: iTerm2, WezTerm, Ghostty, Kitty, Warp, and Windows Terminal support Shift+Enter natively.")}${SLASH_COMMAND_TERMINAL_SETUP_CANNOT_RUN_FROM_TERMINAL_VAR_3}${SLASH_COMMAND_TERMINAL_SETUP_CANNOT_RUN_FROM_TERMINAL_VAR_4()}
