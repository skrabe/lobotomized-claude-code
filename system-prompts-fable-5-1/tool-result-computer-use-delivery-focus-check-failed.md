<!--
name: 'Tool Result: Computer-Use Delivery Focus Check Failed'
description: >-
  Tool result after mid-delivery focus change, saying remaining keystrokes were
  not delivered and to screenshot before retrying.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_DELIVERY_FOCUS_CHECK_FAILED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_DELIVERY_FOCUS_CHECK_FAILED_VAR_1
-->
${TOOL_RESULT_COMPUTER_USE_DELIVERY_FOCUS_CHECK_FAILED_VAR_0?`"${TOOL_RESULT_COMPUTER_USE_DELIVERY_FOCUS_CHECK_FAILED_VAR_1(TOOL_RESULT_COMPUTER_USE_DELIVERY_FOCUS_CHECK_FAILED_VAR_0)}"`:"a different focus state"} only. Take a screenshot to see where focus went and what was actually typed before retrying.
