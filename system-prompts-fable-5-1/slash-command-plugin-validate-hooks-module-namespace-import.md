<!--
name: 'Plugin validate: hook is a namespace import'
description: >-
  Hooks-module scan refusal when a referenced hook is a namespace import rather
  than a function.
ccVersion: 2.1.246
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_NAMESPACE_IMPORT_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_NAMESPACE_IMPORT_VAR_1
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_NAMESPACE_IMPORT_VAR_0} "${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_NAMESPACE_IMPORT_VAR_1.name}" is a namespace import, not a function
