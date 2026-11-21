<!--
name: 'Computer use: Linux dialog restricted'
description: >-
  Refusal returned when input is blocked while a Linux file dialog is open,
  naming the reason and protected files.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_LINUX_DIALOG_RESTRICTED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_LINUX_DIALOG_RESTRICTED_VAR_1
-->
Not allowed while a file dialog is open: ${TOOL_RESULT_COMPUTER_USE_LINUX_DIALOG_RESTRICTED_VAR_0[TOOL_RESULT_COMPUTER_USE_LINUX_DIALOG_RESTRICTED_VAR_1]}. Files that run by themselves later (shell, login and autostart files) are off-limits; ask the user to save such a file, or to click a dialog that these keys do not reach.
