<!--
name: 'Computer use: collision evicted'
description: >-
  Refusal when the user clicked into the app, taking it over, and background
  control was released.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_COLLISION_EVICTED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_COLLISION_EVICTED_VAR_1
-->
The user just clicked into ${TOOL_RESULT_COMPUTER_USE_COLLISION_EVICTED_VAR_0}, taking it over. Background control was released, and I'm backing off from re-acquiring it for ${TOOL_RESULT_COMPUTER_USE_COLLISION_EVICTED_VAR_1}s. Ask the user whether to continue acting on it, or move to a different app.
