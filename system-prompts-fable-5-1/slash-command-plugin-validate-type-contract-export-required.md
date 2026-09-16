<!--
name: 'Plugin Validate: Type Contract Export Required'
description: >-
  Type-contract scan refusal for a top-level type/interface that lacks export
  and would leak into dependents.
ccVersion: 2.1.273
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_EXPORT_REQUIRED_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_EXPORT_REQUIRED_VAR_1
-->
a top-level \`${SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_EXPORT_REQUIRED_VAR_0?.SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_EXPORT_REQUIRED_VAR_1}\` without \`export\` would be global in a dependent's program; export it
