<!--
name: 'Tool Result: Email file reference unknown argument'
description: >-
  Refuses an argument a file-reference email call can't carry and lists the
  allowed argument names
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_UNKNOWN_ARGUMENT_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_UNKNOWN_ARGUMENT_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_UNKNOWN_ARGUMENT_VAR_2
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_UNKNOWN_ARGUMENT_VAR_3
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_UNKNOWN_ARGUMENT_VAR_0} carries ${TOOL_RESULT_EMAIL_FILE_REFERENCE_UNKNOWN_ARGUMENT_VAR_1===""?"an argument with an empty name":`an argument, ${TOOL_RESULT_EMAIL_FILE_REFERENCE_UNKNOWN_ARGUMENT_VAR_2(TOOL_RESULT_EMAIL_FILE_REFERENCE_UNKNOWN_ARGUMENT_VAR_1)},`} that a call attaching files by reference can't carry, ${TOOL_RESULT_EMAIL_FILE_REFERENCE_UNKNOWN_ARGUMENT_VAR_3} Make the call again without it, and put anything it holds that the message needs under one of these names, spelled exactly so in plain ASCII: "to", "cc", "bcc", "subject", "body", "htmlBody", "attachments", "replyToMessageId" and "includeSignature".
