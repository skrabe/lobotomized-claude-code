<!--
name: Interaction Schema Unavailable
description: >-
  Artifact validateInput rejection returned to the model when the named
  interaction schema is not registered in this session, listing the available
  ones.
ccVersion: 2.1.219
variables:
  - TOOL_RESULT_ARTIFACT_INTERACTION_SCHEMA_UNAVAILABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_INTERACTION_SCHEMA_UNAVAILABLE_VAR_1
  - TOOL_RESULT_ARTIFACT_INTERACTION_SCHEMA_UNAVAILABLE_VAR_2
-->
interaction schema "${TOOL_RESULT_ARTIFACT_INTERACTION_SCHEMA_UNAVAILABLE_VAR_0(TOOL_RESULT_ARTIFACT_INTERACTION_SCHEMA_UNAVAILABLE_VAR_1)}" is not available in this session. Available schemas: ${[...TOOL_RESULT_ARTIFACT_INTERACTION_SCHEMA_UNAVAILABLE_VAR_2??[]].join(", ")||"(none)"}.
