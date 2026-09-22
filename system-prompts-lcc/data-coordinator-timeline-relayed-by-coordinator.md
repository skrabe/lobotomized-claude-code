<!--
name: Coordinator timeline message relayed by the session
description: >-
  User-turn provenance marker for a timeline message relayed by the coordinator
  session rather than as a thread reply.
ccVersion: 2.1.268
variables:
  - DATA_COORDINATOR_TIMELINE_RELAYED_BY_COORDINATOR_VAR_0
  - DATA_COORDINATOR_TIMELINE_RELAYED_BY_COORDINATOR_VAR_1
  - DATA_COORDINATOR_TIMELINE_RELAYED_BY_COORDINATOR_VAR_2
-->
${DATA_COORDINATOR_TIMELINE_RELAYED_BY_COORDINATOR_VAR_0} ${DATA_COORDINATOR_TIMELINE_RELAYED_BY_COORDINATOR_VAR_1.written_at} on the timeline (not a reply in this thread) by ${DATA_COORDINATOR_TIMELINE_RELAYED_BY_COORDINATOR_VAR_2(DATA_COORDINATOR_TIMELINE_RELAYED_BY_COORDINATOR_VAR_1)}, relayed by the coordinator session]
