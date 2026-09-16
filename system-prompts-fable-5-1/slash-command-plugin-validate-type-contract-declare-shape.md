<!--
name: 'Plugin Validate: Type Contract Declare Shape'
description: >-
  Type-contract scan refusal when a top-level declare is not `declare module
  'claude-code' { … }` on one line.
ccVersion: 2.1.273
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_DECLARE_SHAPE_VAR_0
-->
\`declare\` at the top level opens only \`declare module '${SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_DECLARE_SHAPE_VAR_0}' { … }\`, its three words on one line
