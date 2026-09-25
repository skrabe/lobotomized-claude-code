<!--
name: 'Slash Command: Plugin Validate — Hooks Module state.set Foreign Owner'
description: >-
  Plugin types/validate problem reported when a hooks module's $.state.set
  writes a key owned by another plugin.
ccVersion: 2.1.282
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1
-->
$.state.set refers to ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_0({plugin:c,key:p})}, which ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1} owns: only a value's owner writes it (to change what is written, hook ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1}'s state.set and rewrite e.value)
