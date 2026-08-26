<!--
name: 'Tool Result: Git Bundle Windows 8.3 Short Names'
description: >-
  Refuses the upload when uncommitted paths look like Windows 8.3 short names
  that can open a different file than they name.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_GIT_BUNDLE_WIN83_SHORT_NAMES_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_WIN83_SHORT_NAMES_VAR_1
-->
Not uploading this working tree: its uncommitted changes include paths shaped like Windows 8.3 short names (${TOOL_RESULT_GIT_BUNDLE_WIN83_SHORT_NAMES_VAR_0(TOOL_RESULT_GIT_BUNDLE_WIN83_SHORT_NAMES_VAR_1)}), which can open a different file than they name. Rename or remove them — committing them as they stand would put whatever they open into git — then retry.
