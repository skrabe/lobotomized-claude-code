<!--
name: 'Tool Description: Memory save step 1 (store document)'
description: >-
  Step 1 of the two-step save procedure in the memory_write prompt
  (store-document variant of the dropped file-based
  system-prompt-memory-save-step1-example-names); tells the model to write the
  memory as its own document with the frontmatter template.
ccVersion: 2.1.224
variables:
  - TOOL_DESCRIPTION_MEMORY_SAVE_STEP1_STORE_VAR_0
-->
**Step 1** — save the memory as its own document in the store with ${TOOL_DESCRIPTION_MEMORY_SAVE_STEP1_STORE_VAR_0}, using this frontmatter format:
