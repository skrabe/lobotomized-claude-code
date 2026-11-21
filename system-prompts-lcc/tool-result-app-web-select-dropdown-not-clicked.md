<!--
name: 'Tool result: app web select dropdown not clicked'
description: >-
  Explains a web <select> was not clicked in the background and how to choose an
  option via app_focus and typing.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_WEB_SELECT_DROPDOWN_NOT_CLICKED_VAR_0
-->
this is a web page's dropdown (a <select>), and opening it in the background would take the keyboard from the app the user is working in, so it was NOT clicked. To choose an option without opening it: app_focus this control, then ${TOOL_RESULT_APP_WEB_SELECT_DROPDOWN_NOT_CLICKED_VAR_0}. If no enabled option begins with that text, nothing changes, so confirm in the picture of a fresh app_screenshot. Where another option begins with the same letters, the page may briefly select that one first: on a page that acts at once on a change (saves, submits, navigates), or if you don't know the options, do not choose an option this way
