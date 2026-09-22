<!--
name: 'Tool Description: memory_list call-early guidance'
description: >-
  Trailing paragraph of the memory_list tool description telling Claude to list
  memories early and always before claiming it lacks information.
ccVersion: 2.1.224
variables:
  - TOOL_DESCRIPTION_MEMORYLIST_CALL_EARLY_GUIDANCE_VAR_0
  - TOOL_DESCRIPTION_MEMORYLIST_CALL_EARLY_GUIDANCE_VAR_1
-->
Call ${TOOL_DESCRIPTION_MEMORYLIST_CALL_EARLY_GUIDANCE_VAR_0} early when context about the project or the work in it would help — and always before telling the user you do not have something. If a listed document looks relevant, ${TOOL_DESCRIPTION_MEMORYLIST_CALL_EARLY_GUIDANCE_VAR_1} it.
