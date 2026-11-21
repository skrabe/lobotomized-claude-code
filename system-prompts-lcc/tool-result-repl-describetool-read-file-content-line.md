<!--
name: 'Tool Result: REPL describeTool Read file content line'
description: >-
  Line substituted into the Read tool description returned by describeTool,
  explaining file.content returns the whole text file without line numbers
ccVersion: 2.1.330
-->
- For a text file on this machine, a script gets the text in `file.content`, with no line numbers: the whole file (up to 256 MiB) unless it passes `offset` or `limit`
