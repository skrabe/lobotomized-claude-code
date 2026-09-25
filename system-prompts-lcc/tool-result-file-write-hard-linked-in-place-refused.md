<!--
name: 'Tool Result: File write refused on hard-linked file'
description: >-
  Error surfaced when an in-place file rewrite is refused because the target has
  other hard-link names, telling the model to remove the extra links and retry
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_FILE_WRITE_HARD_LINKED_IN_PLACE_REFUSED_VAR_0
  - TOOL_RESULT_FILE_WRITE_HARD_LINKED_IN_PLACE_REFUSED_VAR_1
-->
Could not rewrite ${TOOL_RESULT_FILE_WRITE_HARD_LINKED_IN_PLACE_REFUSED_VAR_0} in place: this file has other names on disk (it is hard-linked, ${TOOL_RESULT_FILE_WRITE_HARD_LINKED_IN_PLACE_REFUSED_VAR_1} names in all), and writing it in place would change the file under every one of those names. Remove the extra links, then try again.
