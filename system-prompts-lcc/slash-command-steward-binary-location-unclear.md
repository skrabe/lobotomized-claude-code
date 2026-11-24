<!--
name: 'Slash Command: Steward binary on PATH in a writable place'
description: >-
  Steward refusal template when the git or PowerShell binary Claude Code uses is
  somewhere this session can write
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_BINARY_LOCATION_UNCLEAR_VAR_0
  - SLASH_COMMAND_STEWARD_BINARY_LOCATION_UNCLEAR_VAR_1
-->
the ${SLASH_COMMAND_STEWARD_BINARY_LOCATION_UNCLEAR_VAR_0} that Claude Code uses in this session ${SLASH_COMMAND_STEWARD_BINARY_LOCATION_UNCLEAR_VAR_1}, so it isn't clear what it would do. Change PATH in your shell's profile so that the first ${SLASH_COMMAND_STEWARD_BINARY_LOCATION_UNCLEAR_VAR_0} on it is in another folder, written as a full path, then quit Claude Code and start it again from a new terminal
