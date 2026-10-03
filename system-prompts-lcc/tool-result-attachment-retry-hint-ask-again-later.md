<!--
name: 'Tool Result: Attachment Retry Hint Ask Again Later'
description: >-
  Tail of the transient-upload-failure hint telling the model to say the user
  can ask it to send the attachment(s) again in a few minutes.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_ATTACHMENT_RETRY_HINT_ASK_AGAIN_LATER_VAR_0
  - TOOL_RESULT_ATTACHMENT_RETRY_HINT_ASK_AGAIN_LATER_VAR_1
-->
also tell the user they can ask you to send ${TOOL_RESULT_ATTACHMENT_RETRY_HINT_ASK_AGAIN_LATER_VAR_0(TOOL_RESULT_ATTACHMENT_RETRY_HINT_ASK_AGAIN_LATER_VAR_1.length,"it","them")} again in a few minutes.
