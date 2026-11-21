<!--
name: 'App window put away: bring to current space'
description: >-
  kn arm: call app_bring_to_current_space with window_id; window comes back
  behind without focus.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_WINDOW_PUT_AWAY_BRING_TO_CURRENT_SPACE_VAR_0
-->
To act on it, call app_bring_to_current_space with ${TOOL_RESULT_APP_WINDOW_PUT_AWAY_BRING_TO_CURRENT_SPACE_VAR_0}: the window comes back behind the window the user is working in, and the app does not take keyboard focus
