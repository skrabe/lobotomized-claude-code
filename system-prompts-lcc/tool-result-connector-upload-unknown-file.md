<!--
name: 'Tool result: connector upload unknown file'
description: >-
  Reason: the connector names a fileId that is not one of the call's files with
  bytes to send
ccVersion: 2.1.325
-->
it names a fileId that isn't one of the call's files with bytes to send (Claude Code numbers the call's files file-1, file-2 and so on, skipping any that already stands as text under a key named id in the call's arguments; a file of no bytes gets no upload target)
