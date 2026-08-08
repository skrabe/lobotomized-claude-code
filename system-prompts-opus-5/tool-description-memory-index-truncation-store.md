<!--
name: 'Tool Description: Memory index truncation warning'
description: >-
  Bullet in the memory_write prompt warning the model that the index document is
  loaded into context and truncated past a line cap.
ccVersion: 2.1.224
variables:
  - TOOL_DESCRIPTION_MEMORY_INDEX_TRUNCATION_STORE_VAR_0
-->
- If the index document is shown in your # Memory context, it is loaded into your conversation — lines after ${TOOL_DESCRIPTION_MEMORY_INDEX_TRUNCATION_STORE_VAR_0} are truncated, so keep it concise
