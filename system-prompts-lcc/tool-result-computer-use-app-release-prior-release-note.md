<!--
name: 'Tool result: app_release prior-release note'
description: >-
  Note wrapper in app_release result explaining why background control was
  already released (self-front, third app, or user takeover).
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_APP_RELEASE_PRIOR_RELEASE_NOTE_VAR_0
-->
 Note: ${TOOL_RESULT_COMPUTER_USE_APP_RELEASE_PRIOR_RELEASE_NOTE_VAR_0==="focus_moved_by_target"?"this app had brought itself to the front after the last action":TOOL_RESULT_COMPUTER_USE_APP_RELEASE_PRIOR_RELEASE_NOTE_VAR_0==="focus_moved_to_third"?"the last action here had pushed another app to the front":"the user had clicked into this app, taking it over"} — 
