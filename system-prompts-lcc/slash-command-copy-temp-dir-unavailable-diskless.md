<!--
name: 'Slash Command: /copy temp dir unavailable in diskless session'
description: >-
  Error thrown when the temp directory is requested in a diskless session;
  reaches the model through /copy's 'Failed to write file' onDone output.
ccVersion: 2.1.291
-->
The temp directory is unavailable in a diskless session: nothing is created, verified or written under the shared per-uid temp root
