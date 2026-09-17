<!--
name: 'Tool Description: list_connected_browsers (browser picker guidance)'
description: >-
  Appended to the list_connected_browsers tool description: when to ask the user
  to pick among several connected browsers, how to label the options, and to
  call select_browser or switch_browser rather than choosing one unilaterally
ccVersion: 2.1.274
variables:
  - ASK_USER_TOOL_NAME
  - ASK_USER_QUESTION_TOOL_NAME
  - CHROME_CONFIRMATION_OPTION_LABEL
-->
You do not need to call this before using the browser: when one browser is connected, or one was already chosen for this session, browser tools just work. Only if a browser tool reports that several browsers are connected and none is selected, or the user asks to change browsers, ask with ${ASK_USER_TOOL_NAME(ASK_USER_QUESTION_TOOL_NAME)}: one option per connected browser, the ones on this computer first (display name as the label, deviceId in parentheses), plus a final option labeled exactly: "${CHROME_CONFIRMATION_OPTION_LABEL}" Then call select_browser with the chosen deviceId, or switch_browser for the final option. Never pick one yourself.
