<!--
name: 'Slash Command: Plugin Validate Hooks Module Value Kept Except Catch'
description: >-
  Hooks-module scan refusal: a call's value is kept
  (assigned/passed/read/returned) instead of only using .catch at the call site.
ccVersion: 2.1.267
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_VALUE_KEPT_EXCEPT_CATCH_VAR_0
-->
the value of ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_VALUE_KEPT_EXCEPT_CATCH_VAR_0} is kept (assigned, passed, read, or returned from a nested function); it takes .catch(handler) where it is called and nothing else
