<!--
name: 'Slash Command: /plugin install — Loads In Place Suffix'
description: >-
  Suffix on the plugin already-installed result when the plugin loads in place
  from a local directory. It says edits take effect at the next session start or
  /reload-plugins, and can add how the update command re-records the version.
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_LOADS_IN_PLACE_SUFFIX_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_LOADS_IN_PLACE_SUFFIX_VAR_1
-->
 — it loads in place from ${SLASH_COMMAND_PLUGIN_INSTALL_LOADS_IN_PLACE_SUFFIX_VAR_0}, so edits there take effect at the next session start or /reload-plugins${SLASH_COMMAND_PLUGIN_INSTALL_LOADS_IN_PLACE_SUFFIX_VAR_1}
