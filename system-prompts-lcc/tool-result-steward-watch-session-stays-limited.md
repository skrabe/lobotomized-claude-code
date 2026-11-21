<!--
name: 'Tool Result: Steward watch session stays limited'
description: >-
  Says the session stays under the watch's limits until /steward stop or the end
  command or /clear is typed
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_WATCH_SESSION_STAYS_LIMITED_VAR_0
  - TOOL_RESULT_STEWARD_WATCH_SESSION_STAYS_LIMITED_VAR_1
  - TOOL_RESULT_STEWARD_WATCH_SESSION_STAYS_LIMITED_VAR_2
-->
 Until ${TOOL_RESULT_STEWARD_WATCH_SESSION_STAYS_LIMITED_VAR_0()?"/steward stop":TOOL_RESULT_STEWARD_WATCH_SESSION_STAYS_LIMITED_VAR_1(TOOL_RESULT_STEWARD_WATCH_SESSION_STAYS_LIMITED_VAR_2)} or /clear is typed, this session stays under the watch's limits.
