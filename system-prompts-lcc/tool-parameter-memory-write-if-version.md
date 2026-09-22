<!--
name: 'Tool Parameter: memory_write if_version'
description: >-
  The `if_version` parameter description on the memory_write tool input schema,
  telling the model where the version token comes from and to pass `new` for a
  new file.
ccVersion: 2.1.224
variables:
  - TOOL_PARAMETER_MEMORY_WRITE_IF_VERSION_VAR_0
  - TOOL_PARAMETER_MEMORY_WRITE_IF_VERSION_VAR_1
-->
Pass the 12-character version token from your most recent ${TOOL_PARAMETER_MEMORY_WRITE_IF_VERSION_VAR_0} or ${TOOL_PARAMETER_MEMORY_WRITE_IF_VERSION_VAR_1} of this file. For a file that does not yet exist (not shown in the listing), pass the literal word new (without quotes; an empty string is treated the same way).
