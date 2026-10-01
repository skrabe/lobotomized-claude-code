<!--
name: 'Artifact share: not the owner'
description: >-
  Artifact share permission denial when the person can access but does not own
  the artifact; tells the model to have them ask the owner.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_NOT_OWNER_VAR_0
  - TOOL_RESULT_ARTIFACT_SHARE_NOT_OWNER_VAR_1
  - TOOL_RESULT_ARTIFACT_SHARE_NOT_OWNER_VAR_2
-->
The person can ${TOOL_RESULT_ARTIFACT_SHARE_NOT_OWNER_VAR_0==="writer"?"edit":TOOL_RESULT_ARTIFACT_SHARE_NOT_OWNER_VAR_0==="commenter"?"comment on":TOOL_RESULT_ARTIFACT_SHARE_NOT_OWNER_VAR_0==="reader"?"read":"view"} but does not own the Artifact at ${TOOL_RESULT_ARTIFACT_SHARE_NOT_OWNER_VAR_1}; only its owner can share it from here. ${TOOL_RESULT_ARTIFACT_SHARE_NOT_OWNER_VAR_2} Tell the person to ask its owner${TOOL_RESULT_ARTIFACT_SHARE_NOT_OWNER_VAR_0==="writer"?", or to use the Share menu on claude.ai if their organization lets editors share":""}.
