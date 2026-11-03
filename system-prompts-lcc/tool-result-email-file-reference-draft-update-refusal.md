<!--
name: 'Tool Result: Email file reference draft update refusal'
description: >-
  Refuses attaching files with a draft-update tool because Google keeps unlisted
  recipients, asking for a new draft naming all recipients
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_DRAFT_UPDATE_REFUSAL_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_DRAFT_UPDATE_REFUSAL_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_DRAFT_UPDATE_REFUSAL_VAR_2
-->
Files can't be attached by reference with ${TOOL_RESULT_EMAIL_FILE_REFERENCE_DRAFT_UPDATE_REFUSAL_VAR_0.toolName}, because Google keeps any of the draft's recipients that the call leaves out, and the person approving the call doesn't see those. Nothing was sent to ${TOOL_RESULT_EMAIL_FILE_REFERENCE_DRAFT_UPDATE_REFUSAL_VAR_1} and the draft wasn't changed. Make a new draft with ${TOOL_RESULT_EMAIL_FILE_REFERENCE_DRAFT_UPDATE_REFUSAL_VAR_2.toolName} that names all of its recipients and attaches the files.
