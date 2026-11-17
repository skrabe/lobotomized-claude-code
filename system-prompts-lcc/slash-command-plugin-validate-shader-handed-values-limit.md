<!--
name: 'Shader refusal: handed values limit'
description: >-
  Shader refusal when branches, loops and picks set too many values once
  inlined.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_SHADER_HANDED_VALUES_LIMIT_VAR_0
-->
the branches, loops and picks here set more than ${SLASH_COMMAND_PLUGIN_VALIDATE_SHADER_HANDED_VALUES_LIMIT_VAR_0.handedAProgram} values once every call is inlined: call less, or move repeated work into a for loop
