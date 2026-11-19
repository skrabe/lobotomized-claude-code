<!--
name: 'Tool result: list connected browsers (none selected, some local)'
description: >-
  Reports how many browsers are connected and on this computer, none selected,
  and asks the user to choose starting with local ones
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_LIST_CONNECTED_BROWSERS_NONE_SELECTED_LOCAL_VAR_0
  - TOOL_RESULT_LIST_CONNECTED_BROWSERS_NONE_SELECTED_LOCAL_VAR_1
  - TOOL_RESULT_LIST_CONNECTED_BROWSERS_NONE_SELECTED_LOCAL_VAR_2
  - TOOL_RESULT_LIST_CONNECTED_BROWSERS_NONE_SELECTED_LOCAL_VAR_3
-->
${TOOL_RESULT_LIST_CONNECTED_BROWSERS_NONE_SELECTED_LOCAL_VAR_0.length} browsers are connected, ${TOOL_RESULT_LIST_CONNECTED_BROWSERS_NONE_SELECTED_LOCAL_VAR_1} of them on this computer (onThisComputer: true), and none is selected for this session. ${TOOL_RESULT_LIST_CONNECTED_BROWSERS_NONE_SELECTED_LOCAL_VAR_2(TOOL_RESULT_LIST_CONNECTED_BROWSERS_NONE_SELECTED_LOCAL_VAR_3.askUserToolName)} List the browsers on this computer first.
