<!--
name: 'Tool Result: SendMessage recipient changed by permission handler'
description: >-
  SendMessage failure text stating the permission handler rewrote the recipient
  after the send resolved, so nothing was sent
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_SEND_MESSAGE_PERMISSION_HANDLER_CHANGED_RECIPIENT_VAR_0
-->
The permission handler changed the recipient (from ${TOOL_RESULT_SEND_MESSAGE_PERMISSION_HANDLER_CHANGED_RECIPIENT_VAR_0}) after this send was resolved — nothing was sent. Send again to the recipient you intend.
