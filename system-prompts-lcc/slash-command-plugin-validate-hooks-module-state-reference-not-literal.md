<!--
name: 'Plugin validate: $.state reference not literal'
description: >-
  Hooks-module scan refusal when a $.state call reference lacks string-literal
  plugin and key
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_REFERENCE_NOT_LITERAL_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_REFERENCE_NOT_LITERAL_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_REFERENCE_NOT_LITERAL_VAR_2
-->
$.${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_REFERENCE_NOT_LITERAL_VAR_0} takes a reference whose plugin and key are string literals ({ plugin: "p", key: "k" }, written there or in a const of this file; only id may be computed), so the values a module reads and writes can be listed (got ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_REFERENCE_NOT_LITERAL_VAR_1(SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_REFERENCE_NOT_LITERAL_VAR_2)})
