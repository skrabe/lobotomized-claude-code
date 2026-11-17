<!--
name: '/plugin validate: manifest not read for hooks'
description: >-
  /plugin validate warning that the plugin manifest was not read for the hooks
  files it names, so a hooks module named through it can load unlisted.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MANIFEST_NOT_READ_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MANIFEST_NOT_READ_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MANIFEST_NOT_READ_VAR_2
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MANIFEST_NOT_READ_VAR_0.basename(SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MANIFEST_NOT_READ_VAR_1)} was not read for the hooks files it names: it is a link (a symlink or a Windows junction) or in a linked directory, is not a regular file, could not be opened, or is over ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MANIFEST_NOT_READ_VAR_2} bytes. The plugin loader can still read it, so a hooks module named through it loads without being listed here. Validate a copy of the plugin that holds the real file.
