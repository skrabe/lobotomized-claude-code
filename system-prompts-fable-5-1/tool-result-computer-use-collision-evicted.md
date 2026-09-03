<!--
name: Computer-use collision-evicted backoff
description: >-
  Tool-result telling the model the user took over the app, background control
  was released, and it is backing off before re-acquiring.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_COLLISION_EVICTED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_COLLISION_EVICTED_VAR_1
  - TOOL_RESULT_COMPUTER_USE_COLLISION_EVICTED_VAR_2
-->
The user just clicked into ${TOOL_RESULT_COMPUTER_USE_COLLISION_EVICTED_VAR_0(TOOL_RESULT_COMPUTER_USE_COLLISION_EVICTED_VAR_1)??"this app"}, taking it over. Background control was released, and I'm backing off from re-acquiring it for ${TOOL_RESULT_COMPUTER_USE_COLLISION_EVICTED_VAR_2/1000}s. Ask the user whether to continue acting on it, or move to a different app.
