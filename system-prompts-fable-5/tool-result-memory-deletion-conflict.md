<!--
name: Memory Deletion Concurrent-Write Conflict
description: >-
  Model-facing PostToolUse additionalContext telling the model its memory-file
  deletion was not applied due to a concurrent-write conflict and to re-read and
  delete again.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_MEMORY_DELETION_CONFLICT_VAR_0
-->
Your recent deletion of the memory file ${TOOL_RESULT_MEMORY_DELETION_CONFLICT_VAR_0(TOOL_RESULT_MEMORY_DELETION_CONFLICT_VAR_1)} was NOT applied to shared memory: another session updated the file first (concurrent-write conflict). The file on disk has been restored with the server's current version. Re-read it and delete it again if that is still wanted.
