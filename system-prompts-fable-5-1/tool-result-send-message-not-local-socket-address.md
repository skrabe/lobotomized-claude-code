<!--
name: SendMessage invalid socket address
description: >-
  SendMessage/SendUserFile validateInput error returned to the model when the
  `to` address is not a valid local socket address.
ccVersion: 2.1.210
variables:
  - TOOL_RESULT_SEND_MESSAGE_NOT_LOCAL_SOCKET_ADDRESS_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_NOT_LOCAL_SOCKET_ADDRESS_VAR_1
-->
'${TOOL_RESULT_SEND_MESSAGE_NOT_LOCAL_SOCKET_ADDRESS_VAR_0}' is not a local socket address. Use an address from ${TOOL_RESULT_SEND_MESSAGE_NOT_LOCAL_SOCKET_ADDRESS_VAR_1}.
