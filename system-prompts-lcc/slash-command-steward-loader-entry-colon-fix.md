<!--
name: 'Slash command: steward loader entry colon fix'
description: >-
  Then-arm of Na: explains how to drop an empty colon from a loader path
  variable (profile-line rewrite or sed restart) when it is the only problem
ccVersion: 2.1.332
variables:
  - SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_0
  - SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_1
-->
${SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_0?`A profile line that adds to ${SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_1} before it is set leaves that colon: write \`\${${SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_1}:+:$${SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_1}}\` in place of \`:$${SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_1}\`, or \`\${${SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_1}:+$${SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_1}:}\` in place of \`$${SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_1}:\`, check Claude Code's settings and plugins for it too, and restart Claude Code from a new terminal. Or quit`:"To drop the colon, quit"}, and in this terminal run this, then start the watch again: \`${SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_1}=$(printf %s "$${SLASH_COMMAND_STEWARD_LOADER_ENTRY_COLON_FIX_VAR_1}" | sed -E 's/[:;]+/:/g; s/^:|:$//g') claude --continue\`
