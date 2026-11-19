<!--
name: 'Tool Result: REPL run_in_background unavailable'
description: >-
  REPL inner shell call error saying run_in_background is unavailable and to
  await with a short timeout instead
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_REPL_RUN_IN_BACKGROUND_UNAVAILABLE_VAR_0
-->
${TOOL_RESULT_REPL_RUN_IN_BACKGROUND_UNAVAILABLE_VAR_0.name}: run_in_background is not available in the async REPL. Await the command instead. To keep it running (a dev server, a watcher), give it a short timeout, such as 3000 ms: when the timeout passes, it moves to the background.
