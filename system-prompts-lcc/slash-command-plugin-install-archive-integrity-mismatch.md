<!--
name: 'Slash Command: /plugin install archive integrity mismatch'
description: >-
  Install failure when a downloaded plugin archive's sha256 does not match the
  marketplace entry's pin.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_INTEGRITY_MISMATCH_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_INTEGRITY_MISMATCH_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_INTEGRITY_MISMATCH_VAR_2
-->
Plugin archive integrity check failed for ${SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_INTEGRITY_MISMATCH_VAR_0}: expected sha256 ${SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_INTEGRITY_MISMATCH_VAR_1.sha256.toLowerCase()}, got ${SLASH_COMMAND_PLUGIN_INSTALL_ARCHIVE_INTEGRITY_MISMATCH_VAR_2}. The archive was not installed. Verify the sha256 in the marketplace entry, or that the URL serves the intended file.
