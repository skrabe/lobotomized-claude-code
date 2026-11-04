<!--
name: 'Data: memory sync mass delete batching advice'
description: >-
  Advice appended to the mass-unlink guard notice: to remove many memories, wait
  for restore, then delete at most N at a time with about a minute between
  batches.
ccVersion: 2.1.318
variables:
  - DATA_MEMORY_SYNC_MASS_DELETE_BATCH_ADVICE_VAR_0
  - DATA_MEMORY_SYNC_MASS_DELETE_BATCH_ADVICE_VAR_1
  - DATA_MEMORY_SYNC_MASS_DELETE_BATCH_ADVICE_VAR_2
-->
If you really do intend to remove that many memories, wait until the missing files have been restored, then delete at most ${DATA_MEMORY_SYNC_MASS_DELETE_BATCH_ADVICE_VAR_0} at a time${DATA_MEMORY_SYNC_MASS_DELETE_BATCH_ADVICE_VAR_1(DATA_MEMORY_SYNC_MASS_DELETE_BATCH_ADVICE_VAR_2)?", naming each file by its full path in a command that is only that rm,":""} with about a minute between batches so memory sync can apply each one.
