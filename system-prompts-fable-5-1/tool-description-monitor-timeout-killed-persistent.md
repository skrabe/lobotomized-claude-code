<!--
name: 'Tool Description: Monitor Timeout Killed Persistent'
description: >-
  Monitor tool description copy when persistent watches are available: timeout
  kills the monitor unless persistent:true is set for session-length watches.
ccVersion: 2.1.268
-->
Timeout → killed. Set `persistent: true` for session-length watches (PR monitoring, log tails) — the monitor runs until you call TaskStop or the session ends.
