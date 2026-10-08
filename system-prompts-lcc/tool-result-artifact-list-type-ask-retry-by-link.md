<!--
name: Artifact List Type Ask Retry By Link
description: >-
  Tells the model to retry listing an ask-protected artifact type by its type
  URL.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RETRY_BY_LINK_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RETRY_BY_LINK_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RETRY_BY_LINK_VAR_2
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RETRY_BY_LINK_VAR_3
-->
The permission rule ${TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RETRY_BY_LINK_VAR_0(TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RETRY_BY_LINK_VAR_1)} asks the user before the ${TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RETRY_BY_LINK_VAR_2} type is listed, and the user is asked only when the call names the type by that link, so nothing was listed. To have the user asked, list it again with \`type_url\` set to ${TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RETRY_BY_LINK_VAR_3.found.typeUrl} instead of \`type\`.
