<!--
name: 'Slash Command: plugin validate hooks module duplicate declaration'
description: >-
  /plugin validate refusal for a hooks module in which a name is declared more
  than once, so the declaration hides the top-level function where it is used.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_DUPLICATE_DECLARATION_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_DUPLICATE_DECLARATION_VAR_1
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_DUPLICATE_DECLARATION_VAR_0} "${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_DUPLICATE_DECLARATION_VAR_1.name}" is declared more than once in this file: this declaration hides the top-level function where it is used
