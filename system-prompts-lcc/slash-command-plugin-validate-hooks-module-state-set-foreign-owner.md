<!--
name: 'Slash Command: /plugin validate state.set foreign owner'
description: >-
  /plugin validate finding: a hooks module's state.set refers to a key owned by
  another plugin.
ccVersion: 2.1.292
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1
-->
$.state.set refers to ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_0({plugin:p,key:m})}, which ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1} owns: only a value's owner writes it (to change what is written, hook ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_STATE_SET_FOREIGN_OWNER_VAR_1}'s state.set and rewrite e.value)
