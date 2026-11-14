<!--
name: 'Tool Result: SendUserFile leave file unsent'
description: >-
  Tail of the declined hand-over refusal telling the model to leave the file
  unsent unless the person asks.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_SEND_USER_FILE_LEAVE_UNSENT_VAR_0
-->
 Leave ${TOOL_RESULT_SEND_USER_FILE_LEAVE_UNSENT_VAR_0} unsent, under this or any other name and in any other form, unless the person asks for it. If they do, call SendUserFile again: they are asked again, and only their own pick of Send it sends it.
