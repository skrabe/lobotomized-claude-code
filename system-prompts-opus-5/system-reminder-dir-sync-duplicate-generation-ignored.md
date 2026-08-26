<!--
name: 'System Reminder: Dir Sync Duplicate Generation Ignored'
description: >-
  Tells the cloud agent the user's machine sent two different snapshots under
  the same generation, so the second was ignored and mentioned files may be
  missing.
ccVersion: 2.1.246
-->
Directory sync: the user's machine sent two different snapshots under the same number (another sync process there); this checkout kept the first and ignored the second, so the user's newest edits may be missing until their machine sends a fresh number. Say so if something the user mentions is not here.
