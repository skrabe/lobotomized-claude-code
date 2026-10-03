<!--
name: 'Plugin update: updated to listed commit'
description: >-
  Success result of a plugin update pinned to a directory-listed commit, naming
  the commit prefix, optional version and scope, and asking for a restart.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UPDATE_UPDATED_TO_LISTED_COMMIT_VAR_0
  - SLASH_COMMAND_PLUGIN_UPDATE_UPDATED_TO_LISTED_COMMIT_VAR_1
  - SLASH_COMMAND_PLUGIN_UPDATE_UPDATED_TO_LISTED_COMMIT_VAR_2
  - SLASH_COMMAND_PLUGIN_UPDATE_UPDATED_TO_LISTED_COMMIT_VAR_3
-->
Plugin "${SLASH_COMMAND_PLUGIN_UPDATE_UPDATED_TO_LISTED_COMMIT_VAR_0}" updated to the listed commit ${SLASH_COMMAND_PLUGIN_UPDATE_UPDATED_TO_LISTED_COMMIT_VAR_1.slice(0,7)}${SLASH_COMMAND_PLUGIN_UPDATE_UPDATED_TO_LISTED_COMMIT_VAR_2?` (version ${SLASH_COMMAND_PLUGIN_UPDATE_UPDATED_TO_LISTED_COMMIT_VAR_2})`:""} for scope ${SLASH_COMMAND_PLUGIN_UPDATE_UPDATED_TO_LISTED_COMMIT_VAR_3}. Restart to apply changes.
