<!--
name: 'Slash Command: plugin validate hooks module state.set foreign owner'
description: >-
  Plugin validation problem reported when a hooks module's $.state.set writes a
  value owned by another plugin.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1
-->
$.state.set refers to ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_0({plugin:p,key:f})}, which ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1} owns: only a value's owner writes it (to change what is written, hook ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1}'s state.set and rewrite e.value)
