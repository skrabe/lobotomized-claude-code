<!--
name: Coordinator Timeline Message Attached As The Answered Turn
description: >-
  User-turn provenance marker for a timeline message the server attached to the
  coordinator relay as the user turn the coordinator was answering.
ccVersion: 2.1.269
variables:
  - DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_0
  - DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_1
  - DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_2
-->
${DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_0} ${DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_1.written_at} on the timeline (not a reply in this thread) by ${DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_2(DATA_COORDINATOR_TIMELINE_ATTACHED_AS_ANSWERED_VAR_1)}, attached by the server to the coordinator session's relay as the message the coordinator was answering (the coordinator did not pick it; the words are the user's own, copied by the server)]
