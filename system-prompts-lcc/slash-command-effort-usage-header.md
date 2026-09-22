<!--
name: 'Slash Command: /effort — usage line and level list header'
description: >-
  States the accepted /effort arguments, which the model sees verbatim as
  local-command-stdout and repeats back when the user asks how to change effort.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_EFFORT_USAGE_HEADER_VAR_0
  - SLASH_COMMAND_EFFORT_USAGE_HEADER_VAR_1
-->
Usage: /effort [${SLASH_COMMAND_EFFORT_USAGE_HEADER_VAR_0.join("|")}${SLASH_COMMAND_EFFORT_USAGE_HEADER_VAR_1?"|ultracode":""}|auto]

Effort levels:
