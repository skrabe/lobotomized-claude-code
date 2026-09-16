<!--
name: AppifactRepl Input Contains Invisible Character
description: >-
  AppifactRepl input-schema refine error telling the model to write a hidden
  code point as a \u escape inside a string.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_APPIFACT_REPL_INVISIBLE_CHARACTER_VAR_0
  - TOOL_RESULT_APPIFACT_REPL_INVISIBLE_CHARACTER_VAR_1
-->
input contains an invisible character (U+${TOOL_RESULT_APPIFACT_REPL_INVISIBLE_CHARACTER_VAR_0.padStart(4,"0")}) that the approval dialog would not show; write it as ${TOOL_RESULT_APPIFACT_REPL_INVISIBLE_CHARACTER_VAR_1} inside a string
