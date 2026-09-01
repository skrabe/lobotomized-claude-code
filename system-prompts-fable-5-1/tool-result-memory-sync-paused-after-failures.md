<!--
name: Memory Sync Paused After Failures
description: >-
  PostToolUse additionalContext injected after a memory write warning the model
  that memory sync is paused after repeated failures and recent writes are saved
  locally but not persisted; model-facing.
ccVersion: 2.1.201
variables:
  - TOOL_RESULT_MEMORY_SYNC_PAUSED_AFTER_FAILURES_VAR_0
-->
Memory sync is paused for one of your memory stores after repeated failures (${TOOL_RESULT_MEMORY_SYNC_PAUSED_AFTER_FAILURES_VAR_0}). Recent memory writes are saved locally but are NOT being persisted to shared memory. Sync retries automatically every few minutes.
