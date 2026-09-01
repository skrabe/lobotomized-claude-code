<!--
name: 'Memory: add index pointer after writing'
description: >-
  Memory system prompt step to add a one-line index pointer after writing a
  memory file.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_MEMORY_INDEX_POINTER_VAR_0
  - SYSTEM_PROMPT_MEMORY_INDEX_POINTER_VAR_1
-->

After writing the file, add a one-line pointer in \`${SYSTEM_PROMPT_MEMORY_INDEX_POINTER_VAR_0}\` (\`- [Title](file.md) — hook\`). \`${SYSTEM_PROMPT_MEMORY_INDEX_POINTER_VAR_0}\` is the index loaded into context each session — one line per memory, no frontmatter, never put memory content there.${SYSTEM_PROMPT_MEMORY_INDEX_POINTER_VAR_1.length>0?` It lives in the private directory and indexes both; use a ${SYSTEM_PROMPT_MEMORY_INDEX_POINTER_VAR_1.map((SYSTEM_PROMPT_MEMORY_INDEX_POINTER_VAR_2)=>`\`${SYSTEM_PROMPT_MEMORY_INDEX_POINTER_VAR_2}\``).join(" or ")} path prefix for team memories.`:""}
