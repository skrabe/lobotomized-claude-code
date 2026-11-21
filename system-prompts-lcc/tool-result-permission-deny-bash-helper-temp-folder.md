<!--
name: 'Tool result: Permission deny Bash helper temp folder'
description: >-
  Denial when file tools would write into the temp folder of helper programs run
  before Bash commands
ccVersion: 2.1.330
-->
Claude Code's file tools do not write to this temp folder: it holds helper programs that Bash commands may run first, so a file written here could run with the next command. Write the file somewhere else.
