<!--
name: ClaudeDesign Catalog-Unchanged Note
description: >-
  The `note` field of the catalog_unchanged tool-result object returned by the
  ClaudeDesign tool, telling the model to re-fetch the full operation catalog if
  it fell out of context.
ccVersion: 2.1.207
variables:
  - TOOL_RESULT_CLAUDE_DESIGN_CATALOG_UNCHANGED_NOTE_VAR_0
  - TOOL_RESULT_CLAUDE_DESIGN_CATALOG_UNCHANGED_NOTE_VAR_1
-->
If it is no longer in context, call ${TOOL_RESULT_CLAUDE_DESIGN_CATALOG_UNCHANGED_NOTE_VAR_0}({operation: "${TOOL_RESULT_CLAUDE_DESIGN_CATALOG_UNCHANGED_NOTE_VAR_1}", arguments: {full: true}}) for the full catalog.
