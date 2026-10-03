<!--
name: 'Tool Result: Attachment Images Scaled Down Notice'
description: >-
  Lead line of the tool result saying N attached images were sent to the chat as
  scaled-down copies because the server limits image pixel dimensions.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_ATTACHMENT_IMAGES_SCALED_DOWN_NOTICE_VAR_0
  - TOOL_RESULT_ATTACHMENT_IMAGES_SCALED_DOWN_NOTICE_VAR_1
  - TOOL_RESULT_ATTACHMENT_IMAGES_SCALED_DOWN_NOTICE_VAR_2
-->
${TOOL_RESULT_ATTACHMENT_IMAGES_SCALED_DOWN_NOTICE_VAR_0} ${TOOL_RESULT_ATTACHMENT_IMAGES_SCALED_DOWN_NOTICE_VAR_1(TOOL_RESULT_ATTACHMENT_IMAGES_SCALED_DOWN_NOTICE_VAR_0,"image was sent to the chat as a scaled-down copy","images were sent to the chat as scaled-down copies")}, because the server accepts images at most ${TOOL_RESULT_ATTACHMENT_IMAGES_SCALED_DOWN_NOTICE_VAR_2} pixels wide or tall:
