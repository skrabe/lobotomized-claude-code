<!--
name: 'Tool result: project doc too large, changed nothing'
description: >-
  Projects tool error when a doc exceeds the 1.9 MB limit and cannot be
  rewritten or deleted by tools.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_PROJECT_DOC_TOO_LARGE_CHANGED_NOTHING_VAR_0
-->
This call changed nothing. The doc at this path holds more text than the 1.9 MB limit for one doc, and claude.ai lets no tool ${TOOL_RESULT_PROJECT_DOC_TOO_LARGE_CHANGED_NOTHING_VAR_0} such a doc. The user can still delete it in claude.ai, but this tool cannot bring its text back. A new doc under the limit can still be saved at a new path.
