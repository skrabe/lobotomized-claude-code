<!--
name: 'Slash Command: /plugin validate hook command unquoted placeholder'
description: >-
  Plugin validator warning: a hook shell command uses a path placeholder without
  quotes. It suggests double quotes or exec form.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_COMMAND_UNQUOTED_PLACEHOLDER_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_COMMAND_UNQUOTED_PLACEHOLDER_VAR_1
-->
Shell command uses ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_COMMAND_UNQUOTED_PLACEHOLDER_VAR_0.placeholders.join(", ")} without quotes: ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_COMMAND_UNQUOTED_PLACEHOLDER_VAR_1(SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_COMMAND_UNQUOTED_PLACEHOLDER_VAR_0.command,200)}. If the expanded path contains a space the command can split into several words and fail. Wrap the placeholder in double quotes, or use exec form: {"command": "<executable>", "args": ["\${CLAUDE_PLUGIN_ROOT}/..."]}.
