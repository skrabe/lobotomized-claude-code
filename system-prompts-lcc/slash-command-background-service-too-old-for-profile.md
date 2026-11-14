<!--
name: 'Slash command: /background service too old for profile'
description: >-
  Error returned when the running background service is an older version that
  can't keep this session's profile.
ccVersion: 2.1.325
-->
the background service that is running is an older version, which can't keep this session's profile. Run claude daemon stop --any, which stops background sessions, and try again. If it runs as a service, run claude daemon install instead. Continue a session that was stopped with claude --resume, as you started it
