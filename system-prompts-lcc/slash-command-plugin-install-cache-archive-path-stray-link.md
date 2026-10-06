<!--
name: '/plugin install: stray link at archive path'
description: >-
  Install failure when a link at a plugin's archive path in the cache cannot be
  removed.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_CACHE_ARCHIVE_PATH_STRAY_LINK_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_CACHE_ARCHIVE_PATH_STRAY_LINK_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_CACHE_ARCHIVE_PATH_STRAY_LINK_VAR_2
-->
Could not ${SLASH_COMMAND_PLUGIN_INSTALL_CACHE_ARCHIVE_PATH_STRAY_LINK_VAR_0} ${SLASH_COMMAND_PLUGIN_INSTALL_CACHE_ARCHIVE_PATH_STRAY_LINK_VAR_1} ${SLASH_COMMAND_PLUGIN_INSTALL_CACHE_ARCHIVE_PATH_STRAY_LINK_VAR_2}: a link sits at its archive path and could not be removed; remove that link from the plugin cache, then retry the install.
