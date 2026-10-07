<!--
name: 'Slash Command: Plugin validate hooks module $ callee shadows import'
description: >-
  Hooks-module validation refusal when $ is passed to a name declared again over
  the call, shadowing the import of that name
ccVersion: 2.1.292
variables:
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_DOLLAR_CALLEE_SHADOWS_IMPORT_VAR_0
-->
$ is passed to "${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_DOLLAR_CALLEE_SHADOWS_IMPORT_VAR_0.name}", a name declared again over this call: the engine may not bind it to the import of that name. Rename one of the two
