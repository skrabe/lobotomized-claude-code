<!--
name: 'Slash Command: /terminal-setup Terminal.app restore failed'
description: >-
  /terminal-setup Terminal.app error when restoring preferences from backup
  failed, with the defaults import command to restore manually.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_TERMINAL_SETUP_APPLE_TERMINAL_RESTORE_FAILED_VAR_0
  - SLASH_COMMAND_TERMINAL_SETUP_APPLE_TERMINAL_RESTORE_FAILED_VAR_1
-->
${SLASH_COMMAND_TERMINAL_SETUP_APPLE_TERMINAL_RESTORE_FAILED_VAR_0} Couldn't restore from backup. To restore it yourself, run: defaults import com.apple.Terminal ${SLASH_COMMAND_TERMINAL_SETUP_APPLE_TERMINAL_RESTORE_FAILED_VAR_1.backupPath}
