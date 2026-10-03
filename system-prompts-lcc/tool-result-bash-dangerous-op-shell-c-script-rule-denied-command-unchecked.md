<!--
name: 'Tool Result: shell -c script contains rule-denied command, unchecked'
description: >-
  Permission ask message when a permission rule denies a command inside a shell
  -c script so rm safety could not be checked.
ccVersion: 2.1.288
-->
A permission rule denies a command inside this shell -c script, so Claude Code could not check it for dangerous removals. Approving runs the whole script, including that command.
