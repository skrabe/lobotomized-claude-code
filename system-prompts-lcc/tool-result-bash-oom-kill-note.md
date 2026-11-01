<!--
name: 'Tool result: Bash OOM kill note'
description: >-
  Note appended to Bash output when the kernel killed a process for lack of
  memory during the command.
ccVersion: 2.1.316
-->
[While this command ran, the kernel killed at least one process for lack of memory. All commands in this session share one memory limit. The killed process may have been a worker that a test or build runner replaced, so this output may not show it. It may also have belonged to another command, a background task or another program under the same limit. If this command was the heavy one, run fewer workers in parallel, or a smaller part at a time.]
