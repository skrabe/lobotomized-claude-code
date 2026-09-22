<!--
name: 'Tool Result: Artifact Identical Resubmission Unviewed Source Changed'
description: >-
  identical_resubmission_unviewed refusal when the saved source file was
  modified or removed after it was handed over.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_UNVIEWED_SOURCE_CHANGED_VAR_0
  - TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_UNVIEWED_SOURCE_CHANGED_VAR_1
  - TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_UNVIEWED_SOURCE_CHANGED_VAR_2
  - TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_UNVIEWED_SOURCE_CHANGED_VAR_3
-->
${TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_UNVIEWED_SOURCE_CHANGED_VAR_0}: its saved source ${TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_UNVIEWED_SOURCE_CHANGED_VAR_1.path} was modified or removed after it was handed to you, so Reads of it no longer count. Fetch the artifact's URL again for a fresh copy (if that saves it to a file, Read every line of that file) and, once you have that result, merge anything from it your file lacks and publish again from your own file; if your file already contains that version's content, publishing it unchanged will then go through${TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_UNVIEWED_SOURCE_CHANGED_VAR_2(TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_UNVIEWED_SOURCE_CHANGED_VAR_3)}
