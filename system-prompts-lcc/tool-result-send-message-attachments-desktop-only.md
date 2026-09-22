<!--
name: 'Tool result: Send message attachments desktop only'
description: >-
  Tells the model which attachments never reached Remote Control viewers and to
  explain that to the user
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_SEND_MESSAGE_ATTACHMENTS_DESKTOP_ONLY_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_ATTACHMENTS_DESKTOP_ONLY_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_ATTACHMENTS_DESKTOP_ONLY_VAR_2
-->
Message delivered to user.${TOOL_RESULT_SEND_MESSAGE_ATTACHMENTS_DESKTOP_ONLY_VAR_0}
${TOOL_RESULT_SEND_MESSAGE_ATTACHMENTS_DESKTOP_ONLY_VAR_1.length} ${TOOL_RESULT_SEND_MESSAGE_ATTACHMENTS_DESKTOP_ONLY_VAR_2(TOOL_RESULT_SEND_MESSAGE_ATTACHMENTS_DESKTOP_ONLY_VAR_1.length,"attachment")} NOT delivered to Remote Control (phone/web) viewers — only visible in the desktop app on this machine:
