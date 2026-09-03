<!--
name: 'Data: Memory truncation limit detail'
description: >-
  Byte/line limit clause interpolated into the truncation warning on a partially
  loaded memory file or index
ccVersion: 2.1.219
variables:
  - DATA_MEMORY_TRUNCATION_BYTE_LIMIT_DETAIL_VAR_0
  - DATA_MEMORY_TRUNCATION_BYTE_LIMIT_DETAIL_VAR_1
  - DATA_MEMORY_TRUNCATION_BYTE_LIMIT_DETAIL_VAR_2
  - DATA_MEMORY_TRUNCATION_BYTE_LIMIT_DETAIL_VAR_3
-->
${DATA_MEMORY_TRUNCATION_BYTE_LIMIT_DETAIL_VAR_0(DATA_MEMORY_TRUNCATION_BYTE_LIMIT_DETAIL_VAR_1)} (limit: ${DATA_MEMORY_TRUNCATION_BYTE_LIMIT_DETAIL_VAR_0(DATA_MEMORY_TRUNCATION_BYTE_LIMIT_DETAIL_VAR_2)}) — ${DATA_MEMORY_TRUNCATION_BYTE_LIMIT_DETAIL_VAR_3==="index"?"index entries are too long":"its lines are too long"}
