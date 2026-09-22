<!--
name: 'Slash Command: Plugin Command Run Hook Unanswered'
description: >-
  type:text result of a plugin-registered local slash command that had no
  command.run hook, wrapped as <local-command-stdout> in the conversation.
ccVersion: 2.1.265
variables:
  - SLASH_COMMAND_PLUGIN_COMMAND_RUN_HOOK_UNANSWERED_VAR_0
  - SLASH_COMMAND_PLUGIN_COMMAND_RUN_HOOK_UNANSWERED_VAR_1
-->
${SLASH_COMMAND_PLUGIN_COMMAND_RUN_HOOK_UNANSWERED_VAR_0} registered /${SLASH_COMMAND_PLUGIN_COMMAND_RUN_HOOK_UNANSWERED_VAR_1.name} but no command.run hook answered it: add on("command.run", { command: "${SLASH_COMMAND_PLUGIN_COMMAND_RUN_HOOK_UNANSWERED_VAR_1.name}" }, ($, e) => ({ text: ... })) to the plugin.
