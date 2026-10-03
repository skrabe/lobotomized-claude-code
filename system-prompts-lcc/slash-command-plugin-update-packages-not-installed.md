<!--
name: 'Slash Command: Plugin update packages not installed'
description: >-
  Failure message from a plugin update when the packages the plugin lists for a
  scope could not be installed, with the cause, saying updating again retries.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UPDATE_PACKAGES_NOT_INSTALLED_VAR_0
  - SLASH_COMMAND_PLUGIN_UPDATE_PACKAGES_NOT_INSTALLED_VAR_1
  - SLASH_COMMAND_PLUGIN_UPDATE_PACKAGES_NOT_INSTALLED_VAR_2
  - SLASH_COMMAND_PLUGIN_UPDATE_PACKAGES_NOT_INSTALLED_VAR_3
-->
Could not install the packages that "${SLASH_COMMAND_PLUGIN_UPDATE_PACKAGES_NOT_INSTALLED_VAR_0}" lists for scope ${SLASH_COMMAND_PLUGIN_UPDATE_PACKAGES_NOT_INSTALLED_VAR_1}, so parts of it may not work. Updating it again retries the install.${SLASH_COMMAND_PLUGIN_UPDATE_PACKAGES_NOT_INSTALLED_VAR_2?` Cause: ${SLASH_COMMAND_PLUGIN_UPDATE_PACKAGES_NOT_INSTALLED_VAR_3(SLASH_COMMAND_PLUGIN_UPDATE_PACKAGES_NOT_INSTALLED_VAR_2)}`:""}
