<!--
name: 'Memory Write Warning: Synced Project Store Not Mounted'
description: >-
  Warning injected into the model's context after a Write/Edit whose directory
  belongs to a synced project memory store that is not mounted in this session;
  supersedes 2.1.216's `system-reminder-memory-write-org-store-not-mounted`
  (org-memory → synced project memory rename).
ccVersion: 2.1.218
-->
This file's directory belongs to a synced project memory store that is not mounted in this session. The write was saved locally but is NOT being synced, and a future session with the store mounted will overwrite it with server content. Move the content out of this directory to keep it.
