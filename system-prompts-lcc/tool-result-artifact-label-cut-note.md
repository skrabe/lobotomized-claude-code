<!--
name: 'Tool Result: Artifact Label Cut Note'
description: >-
  Note appended to the Artifact result when coerceInput cut an over-long `label`
  to the maximum length. It reminds Claude that a label is a few words naming
  the version.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_ARTIFACT_LABEL_CUT_NOTE_VAR_0
-->
Note: \`label\` was longer than ${TOOL_RESULT_ARTIFACT_LABEL_CUT_NOTE_VAR_0} characters and was cut to that length; only its start was kept.
