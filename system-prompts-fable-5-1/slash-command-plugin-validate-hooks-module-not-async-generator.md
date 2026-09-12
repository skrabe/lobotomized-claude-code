<!--
name: 'Plugin Validate: Streaming Hook Is Not An Async Generator'
description: >-
  Hooks-module scan refusal when a streaming event's hook is not async
  function*, surfaced through /plugin validate.
ccVersion: 2.1.269
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_NOT_ASYNC_GENERATOR_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_NOT_ASYNC_GENERATOR_VAR_1
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_NOT_ASYNC_GENERATOR_VAR_0} on "${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_NOT_ASYNC_GENERATOR_VAR_1}" is not an async generator: ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_NOT_ASYNC_GENERATOR_VAR_1} streams, so it takes async function* ($, e, next) { ... }, which yields the chunks and returns the result
