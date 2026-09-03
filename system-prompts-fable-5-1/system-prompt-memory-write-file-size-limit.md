<!--
name: Memory Write File Size Limit
description: >-
  System-prompt rule to keep each memory file under a size cap and the
  description to one line.
ccVersion: 2.1.247
variables:
  - SYSTEM_PROMPT_MEMORY_WRITE_FILE_SIZE_LIMIT_VAR_0
  - SYSTEM_PROMPT_MEMORY_WRITE_FILE_SIZE_LIMIT_VAR_1
-->
Keep each memory file under ${SYSTEM_PROMPT_MEMORY_WRITE_FILE_SIZE_LIMIT_VAR_0(SYSTEM_PROMPT_MEMORY_WRITE_FILE_SIZE_LIMIT_VAR_1)} including frontmatter (recall shows only the first ${SYSTEM_PROMPT_MEMORY_WRITE_FILE_SIZE_LIMIT_VAR_0(SYSTEM_PROMPT_MEMORY_WRITE_FILE_SIZE_LIMIT_VAR_1)}) and the description to one specific line; when a file outgrows that, split or summarize it rather than continuing it in a second file.
