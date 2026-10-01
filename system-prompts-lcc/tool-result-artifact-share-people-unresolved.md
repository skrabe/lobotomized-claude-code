<!--
name: 'Tool result: Artifact share people unresolved'
description: >-
  Error thrown by the Artifact share call when a people-mode grant resolved to
  no organization members; tells the model not to guess identifiers or retry
  with different names.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_PEOPLE_UNRESOLVED_VAR_0
-->
No people were confirmed on the card, so nothing was shared. This host must resolve the people you name to organization members and the person picks them on the card; if it cannot, ${TOOL_RESULT_ARTIFACT_SHARE_PEOPLE_UNRESOLVED_VAR_0} Do not guess identifiers or retry with different names unless the person gives them.
