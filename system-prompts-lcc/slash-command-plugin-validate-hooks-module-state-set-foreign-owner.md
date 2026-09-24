<!--
name: 'Slash Command: plugin validate — state.set on another plugin''s value'
description: >-
  Plugin validate error when a hooks module's $.state.set writes a state key
  owned by another plugin, explaining only the owner writes it and how to hook
  its state.set instead.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1
-->
$.state.set refers to ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_0({plugin:p,key:c})}, which ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1} owns: only a value's owner writes it (to change what is written, hook ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1}'s state.set and rewrite e.value)
