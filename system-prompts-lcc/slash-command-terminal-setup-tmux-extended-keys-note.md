<!--
name: 'Slash Command: /terminal-setup tmux extended-keys note'
description: >-
  /terminal-setup note shown inside tmux listing the ~/.tmux.conf lines
  Shift+Enter needs and how to reload them.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_TERMINAL_SETUP_TMUX_EXTENDED_KEYS_NOTE_VAR_0
-->
Inside tmux, Shift+Enter also needs these lines in ~/.tmux.conf:
  ${SLASH_COMMAND_TERMINAL_SETUP_TMUX_EXTENDED_KEYS_NOTE_VAR_0.bold("set -s extended-keys on")}
  ${SLASH_COMMAND_TERMINAL_SETUP_TMUX_EXTENDED_KEYS_NOTE_VAR_0.bold("set -as terminal-features 'xterm*:extkeys'")}
Then run ${SLASH_COMMAND_TERMINAL_SETUP_TMUX_EXTENDED_KEYS_NOTE_VAR_0.bold("tmux source-file ~/.tmux.conf")}, detach and reattach, and restart Claude Code.
