<!--
name: 'Tool result: app listed element covered'
description: >-
  Refusal body when the listed element is covered by another element at its
  position.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_LISTED_ELEMENT_COVERED_VAR_0
  - TOOL_RESULT_APP_LISTED_ELEMENT_COVERED_VAR_1
-->
${TOOL_RESULT_APP_LISTED_ELEMENT_COVERED_VAR_0} is not what is at its position: the app answers with another element there${TOOL_RESULT_APP_LISTED_ELEMENT_COVERED_VAR_1}. Either yours is covered (a label laid over its own checkbox counts), or the page is too busy to say what is on top. Wait until the page has settled, take a fresh app_screenshot, and aim by coordinate at what you see at that place.
