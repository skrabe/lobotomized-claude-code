<!--
name: 'Computer use: collision target came to front'
description: >-
  Refusal when the target app brought itself to the front and background control
  was released.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_COLLISION_FOCUS_MOVED_BY_TARGET_VAR_0
  - TOOL_RESULT_COMPUTER_USE_COLLISION_FOCUS_MOVED_BY_TARGET_VAR_1
-->
After the last action, ${TOOL_RESULT_COMPUTER_USE_COLLISION_FOCUS_MOVED_BY_TARGET_VAR_0} brought itself to the front, which the user will have seen. Background control was released, and I'm backing off from re-acquiring it for ${TOOL_RESULT_COMPUTER_USE_COLLISION_FOCUS_MOVED_BY_TARGET_VAR_1}s. Tell the user what happened and ask whether to continue with this app.
