<!--
name: 'Memory Sync Failure: Mount Dir Unreadable'
description: >-
  Failure-reason text for the `mount_dir_unreadable` pause reason in the
  memory-sync reason map (FMs), interpolated into the "Memory sync is paused …"
  warning that is injected into the model's context as PostToolUse
  additionalContext after a memory-file write.
ccVersion: 2.1.218
-->
A directory inside this memory store's local folder is unreadable (permission denied), so sync cannot verify or persist local files. Fix its permissions; sync then resumes automatically.
