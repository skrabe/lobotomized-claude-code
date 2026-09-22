<!--
name: Coordinator timeline message returned by a tool
description: >-
  User-turn provenance marker for a timeline message the server returned from a
  fetch tool rather than as a thread reply.
ccVersion: 2.1.268
variables:
  - DATA_COORDINATOR_TIMELINE_RETURNED_BY_TOOL_VAR_0
  - DATA_COORDINATOR_TIMELINE_RETURNED_BY_TOOL_VAR_1
  - DATA_COORDINATOR_TIMELINE_RETURNED_BY_TOOL_VAR_2
  - DATA_COORDINATOR_TIMELINE_RETURNED_BY_TOOL_VAR_3
-->
${DATA_COORDINATOR_TIMELINE_RETURNED_BY_TOOL_VAR_0} ${DATA_COORDINATOR_TIMELINE_RETURNED_BY_TOOL_VAR_1.written_at} on the timeline (not a reply in this thread) by ${DATA_COORDINATOR_TIMELINE_RETURNED_BY_TOOL_VAR_2(DATA_COORDINATOR_TIMELINE_RETURNED_BY_TOOL_VAR_1)}, returned by ${DATA_COORDINATOR_TIMELINE_RETURNED_BY_TOOL_VAR_3}]
