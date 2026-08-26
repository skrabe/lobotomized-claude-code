<!--
name: 'Memory write: store read-only'
description: >-
  PostToolUse additionalContext injected to the model warning that the memory
  store is mounted read-only, so the write was saved locally only and will be
  overwritten on next pull.
ccVersion: 2.1.246
-->
This file's memory store is mounted read-only: writes are never synced, and the next sync pull will overwrite local edits with server content. This write was saved locally only and is NOT in shared memory.
