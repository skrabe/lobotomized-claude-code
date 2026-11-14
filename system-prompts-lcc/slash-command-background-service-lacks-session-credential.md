<!--
name: 'Slash command: /background service lacks session credential'
description: >-
  Error returned when the background service doesn't have this session's API
  key, token or workload identity.
ccVersion: 2.1.325
-->
the background service doesn't have this session's API key, token or workload identity, so run it in this terminal. Or, unless the service was set up with claude daemon install, run claude daemon stop --any, which stops every project's background sessions, and try again from here; other background sessions may then use this key, token or identity instead of their own sign-in
