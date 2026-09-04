<!--
name: 'Plugin Validate: $ Is Not Followed Across An Import'
description: >-
  Hooks-module scan refusal when $ is passed to an imported binding; the scanner
  follows only functions declared in the same file.
ccVersion: 2.1.261
variables:
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_DOLLAR_NOT_FOLLOWED_ACROSS_IMPORT_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_DOLLAR_NOT_FOLLOWED_ACROSS_IMPORT_VAR_1
-->
$ is passed to "${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_DOLLAR_NOT_FOLLOWED_ACROSS_IMPORT_VAR_0.name}", imported from "${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_DOLLAR_NOT_FOLLOWED_ACROSS_IMPORT_VAR_1.specifier}": $ is followed only into a function declared in this same file, never across an import
