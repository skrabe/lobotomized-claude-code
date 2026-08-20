<!--
name: 'Tool Result: Unvouched Inbox Pipe'
description: >-
  SendMessage/SendFile error when no running session has registered a live inbox
  at the target pipe, so the send is refused.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_SEND_MESSAGE_UNVOUCHED_PIPE_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_UNVOUCHED_PIPE_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_UNVOUCHED_PIPE_VAR_2
-->
No running session has registered an inbox at ${TOOL_RESULT_SEND_MESSAGE_UNVOUCHED_PIPE_VAR_0} (${TOOL_RESULT_SEND_MESSAGE_UNVOUCHED_PIPE_VAR_1}: ${TOOL_RESULT_SEND_MESSAGE_UNVOUCHED_PIPE_VAR_2.kind}) — refusing to send to an unvouched pipe
