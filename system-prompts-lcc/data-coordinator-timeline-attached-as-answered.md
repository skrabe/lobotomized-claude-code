<!--
name: 'Data: Coordinator timeline message attached as answered'
description: >-
  Provenance marker for a verified user message the server attached to the
  coordinator's relay as the message being answered, noting the coordinator did
  not pick it and the words are the user's own
ccVersion: 2.1.286
variables:
  - DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_0
  - DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_1
  - DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_2
  - DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_3
-->
${DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_0} ${DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_1.written_at} ${DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_2(DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_1)} by ${DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_3(DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_1)}, attached by the server to the coordinator session's relay as the message the coordinator was answering (the coordinator did not pick it; the words are the user's own, copied by the server)]
