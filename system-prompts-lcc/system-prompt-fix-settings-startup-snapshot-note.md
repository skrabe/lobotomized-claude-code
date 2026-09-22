<!--
name: 'Settings-fix prompt: startup-snapshot note'
description: >-
  Conditional note in the buildSettingsFixPrompt user-turn prompt explaining
  that --settings is read at startup and changes take effect in a later session.
ccVersion: 2.1.231
-->
Note: some of these issues are in the file passed via --settings. That file is read once at startup, so after fixing it, tell me the fix takes effect the next time I start a session — the current session keeps the startup snapshot.
