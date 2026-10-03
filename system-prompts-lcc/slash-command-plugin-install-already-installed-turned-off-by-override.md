<!--
name: 'Slash Command: Plugin Install — Already Installed, Turned Off By Override'
description: >-
  Sentence saying the plugin is turned off by managed settings or the --settings
  flag and the command changed nothing.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_ALREADY_INSTALLED_TURNED_OFF_BY_OVERRIDE_VAR_0
-->
 The plugin is turned off by ${SLASH_COMMAND_PLUGIN_INSTALL_ALREADY_INSTALLED_TURNED_OFF_BY_OVERRIDE_VAR_0.override.source==="policySettings"?"your organization's managed settings":"this session's --settings flag"}, and this command changed nothing.
