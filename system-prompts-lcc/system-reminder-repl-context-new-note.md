<!--
name: 'System Reminder: REPL context is new'
description: >-
  Critical system reminder (system message only) injected after a compaction
  when the REPL context was recreated: earlier variables, functions and timers
  are gone; define them again and check whether repeated actions already
  happened.
ccVersion: 2.1.332
-->
This REPL context is new: variables, functions and timers from earlier scripts in this conversation don't exist in it, even those a compaction summary lists as still defined. Define again what you need before you use it. Before you repeat an action from an earlier script, such as writing a file, running a command or sending a message, check whether it already happened.
