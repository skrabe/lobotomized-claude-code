<!--
name: 'Slash Command: plugin validate shader rule: is one of'
description: >-
  Shader validation rule clause reported by plugin validation: "${} is one of
  ${?.(", ")}"
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_SHADER_IS_ONE_OF_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_SHADER_IS_ONE_OF_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_SHADER_IS_ONE_OF_VAR_2
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_SHADER_IS_ONE_OF_VAR_0} is one of ${SLASH_COMMAND_PLUGIN_VALIDATE_SHADER_IS_ONE_OF_VAR_1?.SLASH_COMMAND_PLUGIN_VALIDATE_SHADER_IS_ONE_OF_VAR_2(", ")}
