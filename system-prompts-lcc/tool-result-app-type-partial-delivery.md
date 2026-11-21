<!--
name: 'Tool Result: App Type Partial Delivery'
description: >-
  Error tool_result when background typing is interrupted after part of the text
  was already delivered.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_TYPE_PARTIAL_DELIVERY_VAR_0
-->
Typing was interrupted after the first ${TOOL_RESULT_APP_TYPE_PARTIAL_DELIVERY_VAR_0.deliveredPrefixChars??"few"} characters were already 
