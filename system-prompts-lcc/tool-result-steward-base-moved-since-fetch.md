<!--
name: 'Tool Result: Steward base moved since fetch'
description: >-
  Refuses a base merge when the local ref differs from the base on GitHub and
  asks to refetch
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_BASE_MOVED_SINCE_FETCH_VAR_0
  - TOOL_RESULT_STEWARD_BASE_MOVED_SINCE_FETCH_VAR_1
-->
what ${TOOL_RESULT_STEWARD_BASE_MOVED_SINCE_FETCH_VAR_0} names in this checkout isn't where ${TOOL_RESULT_STEWARD_BASE_MOVED_SINCE_FETCH_VAR_1} stands on GitHub now. It may have moved since your fetch: fetch it again, and run the merge as your very next call. If that fails three times, leave this merge to the user
