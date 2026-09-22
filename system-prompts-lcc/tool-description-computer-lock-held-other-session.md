<!--
name: 'Tool Result: Computer Use Locked By Another Session'
description: >-
  computer-use tool_result when another Claude session holds the computer-use
  lock; tells the model to wait or run /exit there.
ccVersion: 2.1.178
variables:
  - TOOL_DESCRIPTION_COMPUTER_LOCK_HELD_OTHER_SESSION_VAR_0
-->
Computer use is in use by another Claude session (${TOOL_DESCRIPTION_COMPUTER_LOCK_HELD_OTHER_SESSION_VAR_0.slice(0,8)}…). Wait for that session to finish or run /exit there.
