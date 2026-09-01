<!--
name: 'System Reminder: Brief mode toggle'
description: >-
  Announces whether brief mode is enabled and whether user-facing output must
  use the SendUserMessage tool
ccVersion: 2.1.178
variables:
  - IS_BRIEF_MODE_ENABLED
  - SEND_USER_MESSAGE_TOOL_NAME
-->
<system-reminder>
${IS_BRIEF_MODE_ENABLED?`Brief mode is now enabled. Use the ${SEND_USER_MESSAGE_TOOL_NAME} tool for all user-facing output — plain text outside it is hidden from the user's view.`:`Brief mode is now disabled. The ${SEND_USER_MESSAGE_TOOL_NAME} tool is no longer available — reply with plain text.`}
</system-reminder>
