<!--
name: 'Tool result: Send to project reference note (message run)'
description: >-
  For-reference note on a message run saying whether the message was posted and
  that nothing was saved to memory and no setup card posted.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_REFERENCE_MESSAGE_RUN_VAR_0
-->
For your reference only: ${TOOL_RESULT_SEND_TO_PROJECT_REFERENCE_MESSAGE_RUN_VAR_0.message==="sent"?"the message is posted in the project as the user, with this session’s id under it":TOOL_RESULT_SEND_TO_PROJECT_REFERENCE_MESSAGE_RUN_VAR_0.message==="uncertain"?"the message may or may not have been posted":"no message was posted"}; nothing was saved to project memory and no setup card was posted.
