<!--
name: 'System Prompt: Slash command needs an interactive terminal'
description: >-
  Tells the model the command opens an interactive panel that this environment
  cannot show, and that it must be run from the Claude Code terminal.
ccVersion: 2.1.233
variables:
  - SYSTEM_PROMPT_SLASH_COMMAND_NEEDS_INTERACTIVE_TERMINAL_VAR_0
  - SYSTEM_PROMPT_SLASH_COMMAND_NEEDS_INTERACTIVE_TERMINAL_VAR_1
-->
/${SYSTEM_PROMPT_SLASH_COMMAND_NEEDS_INTERACTIVE_TERMINAL_VAR_0(SYSTEM_PROMPT_SLASH_COMMAND_NEEDS_INTERACTIVE_TERMINAL_VAR_1)} opens an interactive panel and isn't available in this environment. Run it from the Claude Code terminal instead.
