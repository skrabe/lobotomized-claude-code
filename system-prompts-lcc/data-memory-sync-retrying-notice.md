<!--
name: Memory sync retrying notice
description: PostToolUse context noting a memory store recently failed and is retrying.
ccVersion: 2.1.206
variables:
  - DATA_MEMORY_SYNC_RETRYING_NOTICE_VAR_0
  - DATA_MEMORY_SYNC_RETRYING_NOTICE_VAR_1
-->
Memory sync for this file's memory store recently failed (${DATA_MEMORY_SYNC_RETRYING_NOTICE_VAR_0.test(DATA_MEMORY_SYNC_RETRYING_NOTICE_VAR_1)?DATA_MEMORY_SYNC_RETRYING_NOTICE_VAR_1:"sync_error"}) and is retrying — recovery is not yet confirmed. 
