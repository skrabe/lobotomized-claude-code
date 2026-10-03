<!--
name: 'Slash Command: Autocompact Window Status'
description: >-
  Text /autocompact prints (and which enters the transcript as
  local-command-stdout) naming the model's settings key and the current
  auto-compact window; the window value is a separate branch expression.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_AUTOCOMPACT_WINDOW_STATUS_VAR_0
  - SLASH_COMMAND_AUTOCOMPACT_WINDOW_STATUS_VAR_1
  - SLASH_COMMAND_AUTOCOMPACT_WINDOW_STATUS_VAR_2
-->
Auto-compact window for ${SLASH_COMMAND_AUTOCOMPACT_WINDOW_STATUS_VAR_0(SLASH_COMMAND_AUTOCOMPACT_WINDOW_STATUS_VAR_1.settingsKey)}: ${SLASH_COMMAND_AUTOCOMPACT_WINDOW_STATUS_VAR_2}
