<!--
name: 'Slash Command: Plugin validate hooks module parameter read shadowed by body'
description: >-
  Hooks-module validation refusal for a name read among a function's parameters
  whose body redeclares it
ccVersion: 2.1.292
variables:
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_PARAMETER_READ_SHADOWED_BY_BODY_VAR_0
-->
"${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_PARAMETER_READ_SHADOWED_BY_BODY_VAR_0.name}" is read among the parameters of a function whose body declares that name again: the engine may bind such a read apart from the text, so the value it names cannot be listed. Rename one of the two
