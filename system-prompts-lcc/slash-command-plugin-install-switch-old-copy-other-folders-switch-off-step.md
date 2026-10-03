<!--
name: 'Slash Command: Plugin Install — Switch, Old Copy Other Folders Switch Off Step'
description: >-
  Per-folder step telling the reader to switch the plugin off in its settings
  file, or to fix the file if it cannot be read.
ccVersion: 2.1.288
variables:
  - >-
    SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_OLD_COPY_OTHER_FOLDERS_SWITCH_OFF_STEP_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_OLD_COPY_OTHER_FOLDERS_SWITCH_OFF_STEP_VAR_1
-->
switch it off in its settings file${SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_OLD_COPY_OTHER_FOLDERS_SWITCH_OFF_STEP_VAR_0?", or fix the file if it cannot be read as settings":SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_OLD_COPY_OTHER_FOLDERS_SWITCH_OFF_STEP_VAR_1?" if it is on there":""}
