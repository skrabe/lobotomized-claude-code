<!--
name: 'Tool Result: Mod theme.set no safe handle'
description: >-
  Error when a mod's theme.set image cannot be read because no safe handle on
  the mod folder is available
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_MOD_THEME_SET_NO_SAFE_HANDLE_VAR_0
  - TOOL_RESULT_MOD_THEME_SET_NO_SAFE_HANDLE_VAR_1
  - TOOL_RESULT_MOD_THEME_SET_NO_SAFE_HANDLE_VAR_2
-->
${TOOL_RESULT_MOD_THEME_SET_NO_SAFE_HANDLE_VAR_0}: ${TOOL_RESULT_MOD_THEME_SET_NO_SAFE_HANDLE_VAR_1} isn't read, so nothing was set: a theme's file is read only through a safe handle on the mod's folder, and Claude Code can't get one here (${TOOL_RESULT_MOD_THEME_SET_NO_SAFE_HANDLE_VAR_2}). If the mod is on a network drive, move it to a local disk
