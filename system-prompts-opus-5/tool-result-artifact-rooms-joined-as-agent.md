<!--
name: Artifact Rooms Joined As Agent
description: >-
  Watches-list tool-result header listing artifact rooms this session joined as
  an agent.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_ARTIFACT_ROOMS_JOINED_AS_AGENT_VAR_0
  - TOOL_RESULT_ARTIFACT_ROOMS_JOINED_AS_AGENT_VAR_1
-->

${TOOL_RESULT_ARTIFACT_ROOMS_JOINED_AS_AGENT_VAR_0.length} artifact ${TOOL_RESULT_ARTIFACT_ROOMS_JOINED_AS_AGENT_VAR_1(TOOL_RESULT_ARTIFACT_ROOMS_JOINED_AS_AGENT_VAR_0.length,"room")} joined as an agent:
