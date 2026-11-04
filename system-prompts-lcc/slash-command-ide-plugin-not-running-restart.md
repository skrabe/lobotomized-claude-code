<!--
name: 'Slash Command: IDE plugin not running, restart'
description: >-
  Says the Claude Code plugin was not found running in the IDE, to install it
  from the JetBrains Marketplace if missing, then restart the IDE and run /ide
  again
ccVersion: 2.1.318
variables:
  - SLASH_COMMAND_IDE_PLUGIN_NOT_RUNNING_RESTART_VAR_0
  - SLASH_COMMAND_IDE_PLUGIN_NOT_RUNNING_RESTART_VAR_1
-->
Couldn't find the Claude Code plugin running in ${SLASH_COMMAND_IDE_PLUGIN_NOT_RUNNING_RESTART_VAR_0.bold(SLASH_COMMAND_IDE_PLUGIN_NOT_RUNNING_RESTART_VAR_1)}.
If it isn't installed, install it from the JetBrains Marketplace.
Then ${SLASH_COMMAND_IDE_PLUGIN_NOT_RUNNING_RESTART_VAR_0.bold(`restart ${SLASH_COMMAND_IDE_PLUGIN_NOT_RUNNING_RESTART_VAR_1}`)} completely and run /ide again.
Installation guide: https://code.claude.com/docs/en/jetbrains#installation
