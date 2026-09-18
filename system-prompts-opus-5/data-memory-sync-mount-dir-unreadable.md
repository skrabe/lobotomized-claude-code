<!--
name: 'Memory Sync Failure: Mount Dir Unreadable'
description: >-
  Failure-reason text for the `mount_dir_unreadable` pause reason in the
  memory-sync reason map (FMs), interpolated into the "Memory sync is paused …"
  warning that is injected into the model's context as PostToolUse
  additionalContext after a memory-file write.
ccVersion: 2.1.276
-->
Part of this memory store's local folder could not be read (for example, permission denied, or a folder removed while sync was reading it), so sync cannot verify or persist local files. Check the folder and its permissions; sync then resumes automatically.
