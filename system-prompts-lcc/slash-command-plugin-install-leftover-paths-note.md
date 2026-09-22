<!--
name: 'Slash Command: /plugin Install Note — Paths Left On Disk'
description: >-
  Sentence appended to the failed plugin-version install error listing leftover
  paths still on disk, which a later install of this version or the plugin cache
  cleanup will remove.
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_LEFTOVER_PATHS_NOTE_VAR_0
-->
 Left on disk (removed by a later install of this version, or the plugin cache cleanup): ${SLASH_COMMAND_PLUGIN_INSTALL_LEFTOVER_PATHS_NOTE_VAR_0.join(", ")}.
