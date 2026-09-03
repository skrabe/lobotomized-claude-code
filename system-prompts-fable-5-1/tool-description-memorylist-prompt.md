<!--
name: 'Tool Description: memory_list prompt'
description: >-
  Tool prompt for listing connected memory stores or store documents, paginating
  and narrowing listings, and directing content reads through memory_read
ccVersion: 2.1.246
variables:
  - MEMORY_READ_TOOL_NAME
-->
List the memory documents in a memory store, sorted by path — each line gives a document's path, size, and last-updated date, but no content (use ${MEMORY_READ_TOOL_NAME} for that). Pass store (the store's id) to choose the store, path_prefix to list one directory, and the cursor from a previous call to continue a long listing. Call with no arguments at all to list the memory stores available in this session — their ids, a one-line description, whether each is writable or read-only, and the path of each store's index document; that set can change during the session, so re-check it whenever you are unsure which store to use.
