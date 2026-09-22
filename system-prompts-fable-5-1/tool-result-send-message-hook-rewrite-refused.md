<!--
name: Send Message Hook Rewrite Refused
description: >-
  SendMessage tool result when a plugin hook rewrites the send into a shape the
  tool refuses.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_SEND_MESSAGE_HOOK_REWRITE_REFUSED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_HOOK_REWRITE_REFUSED_VAR_1
-->
A plugin hook rewrote this send into one the tool refuses (${TOOL_RESULT_SEND_MESSAGE_HOOK_REWRITE_REFUSED_VAR_0?TOOL_RESULT_SEND_MESSAGE_HOOK_REWRITE_REFUSED_VAR_1.message:"a shape SendMessage does not accept"}); nothing was sent.
