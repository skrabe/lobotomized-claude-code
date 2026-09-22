<!--
name: 'Slash Command: /plugin tag — version mismatch'
description: >-
  Error when plugin.json and the marketplace entry disagree on version;
  plugin.json wins at install, so the marketplace entry must be updated before
  tagging.
ccVersion: 2.1.246
variables:
  - SLASH_COMMAND_PLUGIN_TAG_VERSION_MISMATCH_VAR_0
  - SLASH_COMMAND_PLUGIN_TAG_VERSION_MISMATCH_VAR_1
  - SLASH_COMMAND_PLUGIN_TAG_VERSION_MISMATCH_VAR_2
  - SLASH_COMMAND_PLUGIN_TAG_VERSION_MISMATCH_VAR_3
-->
Version mismatch: plugin.json says "${SLASH_COMMAND_PLUGIN_TAG_VERSION_MISMATCH_VAR_0}" but ${SLASH_COMMAND_PLUGIN_TAG_VERSION_MISMATCH_VAR_1(SLASH_COMMAND_PLUGIN_TAG_VERSION_MISMATCH_VAR_2(),SLASH_COMMAND_PLUGIN_TAG_VERSION_MISMATCH_VAR_3.path)} plugins[${SLASH_COMMAND_PLUGIN_TAG_VERSION_MISMATCH_VAR_3.entryIndex}].version says "${SLASH_COMMAND_PLUGIN_TAG_VERSION_MISMATCH_VAR_3.entry.version}". plugin.json wins at install time, so update the marketplace entry to "${SLASH_COMMAND_PLUGIN_TAG_VERSION_MISMATCH_VAR_0}" (or remove it) before tagging.
