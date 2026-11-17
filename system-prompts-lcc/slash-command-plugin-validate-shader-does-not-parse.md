<!--
name: 'Shader refusal: parse error'
description: Shader refusal carrying the cleaned parser error.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_SHADER_DOES_NOT_PARSE_VAR_0
-->
this does not parse: ${SLASH_COMMAND_PLUGIN_VALIDATE_SHADER_DOES_NOT_PARSE_VAR_0.replace(/\$\d+(?![\p{ID_Continue}$])| \((line [^)]*|\d+:\d+)\)/gu,"")}
