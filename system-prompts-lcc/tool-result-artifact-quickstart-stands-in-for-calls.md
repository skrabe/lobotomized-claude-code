<!--
name: 'Tool Result: Quickstart Stands In For Calls'
description: >-
  Tells the model this quickstart result already did the listed
  type/design-system/README calls so it must not repeat them.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_QUICKSTART_STANDS_IN_FOR_CALLS_VAR_0
-->
This one result stands in for ${TOOL_RESULT_ARTIFACT_QUICKSTART_STANDS_IN_FOR_CALLS_VAR_0.length===1?TOOL_RESULT_ARTIFACT_QUICKSTART_STANDS_IN_FOR_CALLS_VAR_0[0]:`${TOOL_RESULT_ARTIFACT_QUICKSTART_STANDS_IN_FOR_CALLS_VAR_0.slice(0,-1).join(", ")} and ${TOOL_RESULT_ARTIFACT_QUICKSTART_STANDS_IN_FOR_CALLS_VAR_0.at(-1)}`} — do not make ${TOOL_RESULT_ARTIFACT_QUICKSTART_STANDS_IN_FOR_CALLS_VAR_0.length===1?"that call":"those calls"} as well.
