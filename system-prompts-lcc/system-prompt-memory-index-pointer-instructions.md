<!--
name: 'System Prompt: Memory index pointer instructions'
description: >-
  Step-2 of the "How to save memories" section for the file-based memory
  directory: add a one-line pointer into the index file, never memory content.
ccVersion: 2.1.224
variables:
  - INDEX_LOCATION_DISPLAY
  - INDEX_FILE
-->
**Step 2** — add a pointer to that file in ${INDEX_LOCATION_DISPLAY}. \`${INDEX_FILE}\` is an index, not a memory — each entry should be one line, under ~150 characters: \`- [Title](file.md) — one-line hook\`. It has no frontmatter. Never write memory content directly into \`${INDEX_FILE}\`.
