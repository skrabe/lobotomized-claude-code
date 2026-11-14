<!--
name: 'Slash command: /reload-plugins load errors suffix'
description: >-
  Suffix on the /reload-plugins result giving the count of errors during load
  and pointing to /plugin.
ccVersion: 2.1.325
variables:
  - SLASH_COMMAND_RELOAD_PLUGINS_LOAD_ERRORS_SUFFIX_VAR_0
  - SLASH_COMMAND_RELOAD_PLUGINS_LOAD_ERRORS_SUFFIX_VAR_1
-->

${SLASH_COMMAND_RELOAD_PLUGINS_LOAD_ERRORS_SUFFIX_VAR_0(SLASH_COMMAND_RELOAD_PLUGINS_LOAD_ERRORS_SUFFIX_VAR_1,"error")} during load. Run /plugin for details.
