<!--
name: 'Tool Result: Artifact Describe Type Instructions Ships'
description: >-
  describe_type line when the type ships an instructions file, noting that a
  create result carries it.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_INSTRUCTIONS_SHIPS_VAR_0
  - TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_INSTRUCTIONS_SHIPS_VAR_1
-->
Instructions: ships ${TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_INSTRUCTIONS_SHIPS_VAR_0}${typeof TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_INSTRUCTIONS_SHIPS_VAR_1.instructions==="string"?" — below":""}${TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_INSTRUCTIONS_SHIPS_VAR_2?typeof TOOL_RESULT_ARTIFACT_DESCRIBE_TYPE_INSTRUCTIONS_SHIPS_VAR_1.instructions==="string"?"; a create result carries it too":" — a create result carries it":""}.
