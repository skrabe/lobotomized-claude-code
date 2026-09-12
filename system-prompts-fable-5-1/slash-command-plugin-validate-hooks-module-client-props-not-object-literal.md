<!--
name: 'Slash Command: Plugin Validate Hooks Module Client Props Not Object Literal'
description: >-
  Hooks-module scan refusal: Client() must take an object literal so the named
  surface module can be read before it runs.
ccVersion: 2.1.269
variables:
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_CLIENT_PROPS_NOT_OBJECT_LITERAL_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_CLIENT_PROPS_NOT_OBJECT_LITERAL_VAR_1
-->
Client takes its props as an object literal ({ module: "./board.tsx", key }), so the surface module it names can be read before it runs (got ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_CLIENT_PROPS_NOT_OBJECT_LITERAL_VAR_0(SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_CLIENT_PROPS_NOT_OBJECT_LITERAL_VAR_1)})
