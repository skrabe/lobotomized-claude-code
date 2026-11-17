<!--
name: 'Local command output: check settings files after failed permission save'
description: >-
  Follow-up advice to check the settings file(s) hold valid JSON and are
  writable, then restart and redo the change.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_PERMISSION_SAVE_CHECK_FILES_VAR_0
-->
Check that ${SLASH_COMMAND_PERMISSION_SAVE_CHECK_FILES_VAR_0.length>1?"each file":"the file"} holds valid JSON and that you can write to it and its folder, then restart Claude Code and make the change again.
