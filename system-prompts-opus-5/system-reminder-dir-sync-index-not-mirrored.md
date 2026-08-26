<!--
name: 'System Reminder: Dir Sync Index Not Mirrored'
description: >-
  Tells the cloud agent the index could not be updated to the user's staging and
  how to re-sync it with git reset.
ccVersion: 2.1.246
-->
The index could not be updated to the user's staging, so `git status` may show stale staged changes; `git reset` (no arguments) re-synchronises it with HEAD without touching files.
