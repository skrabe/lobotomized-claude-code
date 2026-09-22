<!--
name: loop.md truncation warning
description: >-
  Truncated loop.md content plus a byte-limit warning, injected into the model
  as the ${.content} portion of the /loop tick prompt.
ccVersion: 2.1.206
variables:
  - DATA_LOOP_MD_TRUNCATION_WARNING_VAR_0
  - DATA_LOOP_MD_TRUNCATION_WARNING_VAR_1
  - DATA_LOOP_MD_TRUNCATION_WARNING_VAR_2
-->
${DATA_LOOP_MD_TRUNCATION_WARNING_VAR_0.slice(0,DATA_LOOP_MD_TRUNCATION_WARNING_VAR_1>0?DATA_LOOP_MD_TRUNCATION_WARNING_VAR_1:DATA_LOOP_MD_TRUNCATION_WARNING_VAR_2)}

> WARNING: loop.md was truncated to ${DATA_LOOP_MD_TRUNCATION_WARNING_VAR_2} bytes. Keep the task list concise.
