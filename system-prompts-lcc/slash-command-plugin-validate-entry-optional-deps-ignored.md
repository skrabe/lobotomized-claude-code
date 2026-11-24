<!--
name: 'Plugin validate: entry optionalDependencies ignored'
description: >-
  Validation warning that the marketplace entry's optionalDependencies is
  ignored since the plugin has its own plugin.json.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_ENTRY_OPTIONAL_DEPS_IGNORED_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_ENTRY_OPTIONAL_DEPS_IGNORED_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_ENTRY_OPTIONAL_DEPS_IGNORED_VAR_2
-->
This plugin has its own plugin.json, so the entry's list is ignored. Move it to ${SLASH_COMMAND_PLUGIN_VALIDATE_ENTRY_OPTIONAL_DEPS_IGNORED_VAR_0.relative(SLASH_COMMAND_PLUGIN_VALIDATE_ENTRY_OPTIONAL_DEPS_IGNORED_VAR_1,SLASH_COMMAND_PLUGIN_VALIDATE_ENTRY_OPTIONAL_DEPS_IGNORED_VAR_2)}.
