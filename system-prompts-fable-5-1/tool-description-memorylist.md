<!--
name: 'Tool Description: memory_list'
description: >-
  memory_list tool description covering path-prefix listings, pagination, and
  listing the session's memory stores when called with no arguments.
ccVersion: 2.1.246
variables:
  - TOOL_DESCRIPTION_MEMORYLIST_VAR_0
-->
List memory documents (optionally under a path prefix), sorted by path. Returns path, size, and last-updated time for each. Results are capped; use cursor to page through large stores, or narrow with path_prefix. Use ${TOOL_DESCRIPTION_MEMORYLIST_VAR_0} for content. Pass store (a store's id) to list that store; call with no arguments to list the memory stores available in this session — their ids, a one-line description, whether each is writable or read-only, and the path of each store's index document.
