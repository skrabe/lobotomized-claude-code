<!--
name: 'Local Command: /background API key not bare'
description: >-
  Refusal returned by /background or /fork when a new background session cannot
  reuse this session's unapproved API key because it is not --bare
ccVersion: 2.1.326
-->
a background session started from here isn't --bare, so it can't use this session's API key, which nobody approved. Run it in this terminal. A new one started with claude --bare --bg gets the key only if the background service has it or isn't running yet
