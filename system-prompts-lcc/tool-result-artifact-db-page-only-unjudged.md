<!--
name: 'Tool Result: Artifact DB page-only unjudged write'
description: >-
  Server could not tell which documents a write touches; server bug, tell the
  user
ccVersion: 2.1.322
-->
This artifact keeps some documents for its own page, and the server could not work out which documents this call writes. This is a server bug, not a problem with the call, and a retry will fail the same way. Tell the user that the write failed because of a server error
