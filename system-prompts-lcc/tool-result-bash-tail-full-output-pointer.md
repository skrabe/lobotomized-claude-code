<!--
name: 'Tool Result: Bash tail full output pointer'
description: >-
  Bash result note, for a command piped into tail, giving the size and path of
  the full output (or full input to tail) and telling the model to read it
  instead of re-running
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_BASH_TAIL_FULL_OUTPUT_POINTER_VAR_0
-->
${TOOL_RESULT_BASH_TAIL_FULL_OUTPUT_POINTER_VAR_0?"Full output":"Full input to tail"} ({size}): {path} Read it instead of re-running.
