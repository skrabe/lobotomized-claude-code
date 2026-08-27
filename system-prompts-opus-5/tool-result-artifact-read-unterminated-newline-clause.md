<!--
name: Artifact Read Unterminated Newline Clause
description: >-
  Parenthetical on an artifact-read tool result when the saved file has no
  trailing newline, so wc -l under-counts and the model must Read every line.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_ARTIFACT_READ_UNTERMINATED_NEWLINE_CLAUSE_VAR_0
-->
; the last has no trailing newline, so \`wc -l\` reports ${TOOL_RESULT_ARTIFACT_READ_UNTERMINATED_NEWLINE_CLAUSE_VAR_0-1} — Read through line ${TOOL_RESULT_ARTIFACT_READ_UNTERMINATED_NEWLINE_CLAUSE_VAR_0} and leave the file as it is
