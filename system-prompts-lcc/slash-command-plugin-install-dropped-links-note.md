<!--
name: 'Plugin install: dropped links note'
description: >-
  Note after a plugin install that some symbolic links were dropped because they
  lead outside the plugin or cannot be checked.
ccVersion: 2.1.332
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_DROPPED_LINKS_NOTE_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_DROPPED_LINKS_NOTE_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_DROPPED_LINKS_NOTE_VAR_2
-->
Note: "${SLASH_COMMAND_PLUGIN_INSTALL_DROPPED_LINKS_NOTE_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_DROPPED_LINKS_NOTE_VAR_1.name,120)}" was installed without ${SLASH_COMMAND_PLUGIN_INSTALL_DROPPED_LINKS_NOTE_VAR_2.droppedLinks===1?"1 link it can't keep, because the link leads outside the plugin or can't be checked. Anything that uses that link won't work. The plugin's author can replace it":`${SLASH_COMMAND_PLUGIN_INSTALL_DROPPED_LINKS_NOTE_VAR_2.droppedLinks} links it can't keep, because they lead outside the plugin or can't be checked. Anything that uses them won't work. The plugin's author can replace them`} with real files
