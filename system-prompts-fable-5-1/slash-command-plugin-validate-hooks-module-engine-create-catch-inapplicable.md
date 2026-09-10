<!--
name: 'Plugin Validate: Engine.create Hook Catch Does Not Apply'
description: >-
  Hooks-module scan refusal when .catch() is used on an engine.create hook that
  has no budget.
ccVersion: 2.1.267
variables:
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_ENGINE_CREATE_CATCH_INAPPLICABLE_VAR_0
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_ENGINE_CREATE_CATCH_INAPPLICABLE_VAR_0}.catch(): an engine.create hook has no budget and its failure fails the load; .catch does not apply
