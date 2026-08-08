<!--
name: 'Tool Result: memory_write secret refused'
description: >-
  Refusal returned to the model when memory_write content trips the secret
  detector for a store shared across the organization's projects.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_WRITE_SECRET_REFUSED_VAR_0
  - TOOL_RESULT_MEMORY_WRITE_SECRET_REFUSED_VAR_1
-->
Content contains potential secrets (${TOOL_RESULT_MEMORY_WRITE_SECRET_REFUSED_VAR_0.map((TOOL_RESULT_MEMORY_WRITE_SECRET_REFUSED_VAR_1)=>TOOL_RESULT_MEMORY_WRITE_SECRET_REFUSED_VAR_1.label).join(", ")}) and cannot be written to shared memory. Remove the sensitive content and try again.
