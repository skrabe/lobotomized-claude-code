<!--
name: Command writes to .git/
description: >-
  Command-safety approval reason surfaced to the model when a command writes to
  .git/ where hooks/config may execute.
ccVersion: 2.1.206
-->
Command writes to .git/ — hooks or config planted there execute on the next git operation.
