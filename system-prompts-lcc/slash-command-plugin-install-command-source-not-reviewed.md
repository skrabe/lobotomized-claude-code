<!--
name: 'Slash Command: /plugin install command source not reviewed'
description: >-
  Install refusal when a plugin (e.g. a dependency) is sourced by running an
  unreviewed command on the machine; tells to review and accept it from the
  /plugin details pane or a terminal.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_COMMAND_SOURCE_NOT_REVIEWED_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_COMMAND_SOURCE_NOT_REVIEWED_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_COMMAND_SOURCE_NOT_REVIEWED_VAR_2
  - SLASH_COMMAND_PLUGIN_INSTALL_COMMAND_SOURCE_NOT_REVIEWED_VAR_3
-->
${SLASH_COMMAND_PLUGIN_INSTALL_COMMAND_SOURCE_NOT_REVIEWED_VAR_0} is installed by running a command on this machine (\`${SLASH_COMMAND_PLUGIN_INSTALL_COMMAND_SOURCE_NOT_REVIEWED_VAR_1}\`) that has not been reviewed yet, so it was not run. Review and accept it from its /plugin details pane, or in a terminal: ${SLASH_COMMAND_PLUGIN_INSTALL_COMMAND_SOURCE_NOT_REVIEWED_VAR_2("plugin install",SLASH_COMMAND_PLUGIN_INSTALL_COMMAND_SOURCE_NOT_REVIEWED_VAR_3,{fallback:"an explicit plugin install reviews it"})}.
