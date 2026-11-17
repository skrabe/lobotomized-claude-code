<!--
name: 'Tool Result: search refused through /proc or /dev link'
description: >-
  Error when the search path is or leads to a /proc or /dev link the tool won't
  search through; give the folder's own path.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_SEARCH_PROC_DEV_LINK_REFUSED_VAR_0
  - TOOL_RESULT_SEARCH_PROC_DEV_LINK_REFUSED_VAR_1
  - TOOL_RESULT_SEARCH_PROC_DEV_LINK_REFUSED_VAR_2
-->
Cannot search '${TOOL_RESULT_SEARCH_PROC_DEV_LINK_REFUSED_VAR_0(TOOL_RESULT_SEARCH_PROC_DEV_LINK_REFUSED_VAR_1.path??TOOL_RESULT_SEARCH_PROC_DEV_LINK_REFUSED_VAR_2)}': it is or leads to a /proc or /dev link that this tool does not search through. Give the folder's own path.
