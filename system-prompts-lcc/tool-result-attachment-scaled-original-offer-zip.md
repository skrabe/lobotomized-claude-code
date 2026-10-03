<!--
name: 'Tool Result: Attachment Scaled Original Offer Zip'
description: >-
  Clause telling the model that if the user needs the full-size original(s) it
  should offer to send them inside a .zip.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_ATTACHMENT_SCALED_ORIGINAL_OFFER_ZIP_VAR_0
  - TOOL_RESULT_ATTACHMENT_SCALED_ORIGINAL_OFFER_ZIP_VAR_1
-->
if they need ${TOOL_RESULT_ATTACHMENT_SCALED_ORIGINAL_OFFER_ZIP_VAR_0(TOOL_RESULT_ATTACHMENT_SCALED_ORIGINAL_OFFER_ZIP_VAR_1,"the full-size original","a full-size original")}, offer to send it inside a .zip.
