<!--
name: 'Plugin Validate: Type Contract Unclosed Declare Module'
description: Type-contract scan refusal when a declare module block never lexically closes.
ccVersion: 2.1.273
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_DECLARE_UNCLOSED_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_DECLARE_UNCLOSED_VAR_1
-->
line ${SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_DECLARE_UNCLOSED_VAR_0?.SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_DECLARE_UNCLOSED_VAR_1}: \`declare module\` never closes: the text does not lex as a type contract, so the check refuses it
