<!--
name: 'Plugin Validate: Type Contract Wrong Module Name'
description: >-
  Type-contract scan refusal when declare module names anything other than
  'claude-code'.
ccVersion: 2.1.273
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_WRONG_MODULE_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_WRONG_MODULE_VAR_1
-->
augments module '${SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_WRONG_MODULE_VAR_0.text}'; the contract may only augment '${SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_WRONG_MODULE_VAR_1}'
