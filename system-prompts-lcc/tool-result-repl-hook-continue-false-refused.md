<!--
name: 'Tool result: REPL hook continue false refused'
description: >-
  Tool result for further tool calls from a script after a hook returned
  continue: false
ccVersion: 2.1.318
-->
This tool call did not run. A hook returned continue: false for another tool call from the same piece of code, so every further tool call from it is refused. The hook's reason is sent with that code's result.
