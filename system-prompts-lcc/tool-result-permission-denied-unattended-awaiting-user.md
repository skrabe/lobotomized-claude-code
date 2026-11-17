<!--
name: 'Tool Result: permission denied, user away'
description: >-
  Deny message when a call needs approval but the user has not written since a
  non-user turn started: keep going on work needing no approval and say what is
  waiting.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_PERMISSION_DENIED_UNATTENDED_AWAITING_USER_VAR_0
  - TOOL_RESULT_PERMISSION_DENIED_UNATTENDED_AWAITING_USER_VAR_1
-->
${TOOL_RESULT_PERMISSION_DENIED_UNATTENDED_AWAITING_USER_VAR_0}, and the user has not written since something other than their message opened a turn, so nobody may be here to give one. You can go on with work that needs no approval. The user reads your reply when they come back: if it says what is waiting, they can tell you whether to go ahead, and after their message you can make the call again. What is waiting: ${TOOL_RESULT_PERMISSION_DENIED_UNATTENDED_AWAITING_USER_VAR_1}
