<!--
name: '/plugin install: installed copy in use'
description: >-
  Install failure when the installed copy of a plugin version cannot be replaced
  because it is in use or not modifiable.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_INSTALLED_COPY_IN_USE_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_INSTALLED_COPY_IN_USE_VAR_1
-->
The installed copy of this plugin version at ${SLASH_COMMAND_PLUGIN_INSTALL_INSTALLED_COPY_IN_USE_VAR_0} could not be replaced: it is in use by another program (for example a running Claude Code session, or an editor or terminal inside that folder), or this account is not allowed to modify it (${SLASH_COMMAND_PLUGIN_INSTALL_INSTALLED_COPY_IN_USE_VAR_1}). It was not replaced and the new copy was discarded. Close what is using it, or check the folder's permissions, and run the install again.
