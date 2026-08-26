<!--
name: Coordinator timeline ask is not the user
description: >-
  Assistant-turn prefix marking a prior timeline ask as the coordinator's words,
  not the user's, immediately before the user's reply.
ccVersion: 2.1.246
variables:
  - DATA_COORDINATOR_TIMELINE_ASK_NOT_USER_VAR_0
  - DATA_COORDINATOR_TIMELINE_ASK_NOT_USER_VAR_1
  - DATA_COORDINATOR_TIMELINE_ASK_NOT_USER_VAR_2
  - DATA_COORDINATOR_TIMELINE_ASK_NOT_USER_VAR_3
-->
${DATA_COORDINATOR_TIMELINE_ASK_NOT_USER_VAR_0} written ${DATA_COORDINATOR_TIMELINE_ASK_NOT_USER_VAR_1.written_at}${DATA_COORDINATOR_TIMELINE_ASK_NOT_USER_VAR_2(DATA_COORDINATOR_TIMELINE_ASK_NOT_USER_VAR_1)} (the coordinator's words, not the user's). The user's next timeline message, written ${DATA_COORDINATOR_TIMELINE_ASK_NOT_USER_VAR_3.written_at}${DATA_COORDINATOR_TIMELINE_ASK_NOT_USER_VAR_2(DATA_COORDINATOR_TIMELINE_ASK_NOT_USER_VAR_3)} and shown below, directly followed it.
