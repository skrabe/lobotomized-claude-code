<!--
name: 'Tool Result: Auto mode refuses hook-changed code'
description: >-
  Deny reason when auto mode will not run REPL code that a hook changed (or an
  earlier call in the response was changed).
ccVersion: 2.1.318
-->
Auto mode does not run code after a hook changed it, or changed an earlier tool call in the same response. Turn the hook off, or leave auto mode, where you are asked about each of the code's tool calls that needs approval.
