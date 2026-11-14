<!--
name: 'Tool Result: artifact conflict changed files named'
description: >-
  Artifact publish conflict result listing which files a newer live version
  changed that this publish writes or removes, telling the model to re-read
  each, re-apply its change and publish again.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_0
  - TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_1
  - TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_2
  - TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_3
  - TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_4
-->
${TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_0} changed ${TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_1(TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_2.length,"a file","files")} this publish writes or removes: ${TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_3.join(", ")}${TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_4>0?` and ${TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_4} more`:""}. Read ${TOOL_RESULT_ARTIFACT_CONFLICT_CHANGED_FILES_NAMED_VAR_2.length===1?"it":"each one"} again, re-apply your change to what it holds now, and publish again.
