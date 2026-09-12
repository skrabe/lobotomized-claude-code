<!--
name: 'Plugin Validate: Non-Streaming Hook Is An Async Generator'
description: >-
  Hooks-module scan refusal when a non-streaming event's hook is an async
  generator, surfaced through /plugin validate.
ccVersion: 2.1.269
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_UNEXPECTED_ASYNC_GENERATOR_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_UNEXPECTED_ASYNC_GENERATOR_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_UNEXPECTED_ASYNC_GENERATOR_VAR_2
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_UNEXPECTED_ASYNC_GENERATOR_VAR_0} on "${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_UNEXPECTED_ASYNC_GENERATOR_VAR_1}" is an async generator: only a streaming event named as itself (${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_UNEXPECTED_ASYNC_GENERATOR_VAR_2.join(", ")}) takes one; this pattern takes ($, e, next) => result
