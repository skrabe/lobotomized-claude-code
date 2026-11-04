<!--
name: 'Tool result: REPL leftover code stopped'
description: >-
  Late-output note that finished code left a loop/promise chain making calls
  which now get no answer and was stopped; resend steps in awaited code.
ccVersion: 2.1.318
-->
Code that had already finished left a loop or promise chain running, and it kept making calls. Finished code can run no tool, so its calls now get no answer and it has stopped. To run these steps, send them again in one piece of code that awaits each of them.
