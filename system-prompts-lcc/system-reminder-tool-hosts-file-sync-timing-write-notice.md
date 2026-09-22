<!--
name: 'System Reminder: Tool Hosts File Sync Timing Write Notice'
description: >-
  Main-turn file-sync timing: writes land before the result (Directory sync
  line), read-only changes before the next step with a notice.
ccVersion: 2.1.261
-->
is sent back as it finishes — for a command that writes, before you see its result (a "Directory sync:" line under the result says what came); for a read-only one, before your next step, with a notice.
