<!--
name: 'Plugin validate: state const not frozen'
description: >-
  Hooks-module scan refusal when a const used as a $.state reference is also
  written, passed on or exported
ccVersion: 2.1.281
variables:
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_CONST_REFERENCE_NOT_FROZEN_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_CONST_REFERENCE_NOT_FROZEN_VAR_1
-->
the const ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_CONST_REFERENCE_NOT_FROZEN_VAR_0.read.name}, read as the reference of a $.${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_CONST_REFERENCE_NOT_FROZEN_VAR_1} call, is also written through, handed on or exported here, and const does not freeze: what it holds at the call could not be listed. Use it only as the reference of $.state calls, as a source of the state library's functions imported from "claude-code", and in a spread into an object literal ({ ...${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_CONST_REFERENCE_NOT_FROZEN_VAR_0.read.name}, id }), or write the reference at the call
