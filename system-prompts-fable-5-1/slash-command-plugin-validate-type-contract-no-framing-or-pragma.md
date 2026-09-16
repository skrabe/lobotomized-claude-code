<!--
name: 'Plugin Validate: Type Contract Forbids Framing Or Pragma Lines'
description: >-
  Type-contract scan refusal for a line that would look like the roll-up banner
  or a @ts- pragma once copied.
ccVersion: 2.1.273
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_NO_FRAMING_OR_PRAGMA_VAR_0
-->
line ${SLASH_COMMAND_PLUGIN_VALIDATE_TYPE_CONTRACT_NO_FRAMING_OR_PRAGMA_VAR_0+1}: a line that would read as the roll-up's framing or a compiler pragma once copied; a contract carries neither
