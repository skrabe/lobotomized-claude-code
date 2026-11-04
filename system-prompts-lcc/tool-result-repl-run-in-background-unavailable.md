<!--
name: 'REPL: run_in_background Unavailable In Async REPL'
description: >-
  Refusal when a shell call in the async REPL sets run_in_background; tells the
  script to await the command instead.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_RUN_IN_BACKGROUND_UNAVAILABLE_VAR_0
-->
${TOOL_RESULT_REPL_RUN_IN_BACKGROUND_UNAVAILABLE_VAR_0.name}: run_in_background is not available in the async REPL. The eval already runs in the background, so await the command instead.
