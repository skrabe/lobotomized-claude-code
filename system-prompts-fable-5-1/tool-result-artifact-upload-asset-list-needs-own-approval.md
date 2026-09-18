<!--
name: Artifact Upload Asset List Needs Own Approval
description: >-
  checkPermissions deny when some file_paths entries need their own approval, so
  nothing was uploaded.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_LIST_NEEDS_OWN_APPROVAL_VAR_0
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_LIST_NEEDS_OWN_APPROVAL_VAR_1
-->
${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_LIST_NEEDS_OWN_APPROVAL_VAR_0?"One file":`${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_LIST_NEEDS_OWN_APPROVAL_VAR_1.length} files`} in \`file_paths\` ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_LIST_NEEDS_OWN_APPROVAL_VAR_0?"needs":"need"} an approval of ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_LIST_NEEDS_OWN_APPROVAL_VAR_0?"its":"their"} own, so nothing was uploaded: ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_LIST_NEEDS_OWN_APPROVAL_VAR_1.join("; ")}. Upload ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_LIST_NEEDS_OWN_APPROVAL_VAR_0?"it":"each of those"} in its own call with \`file_path\`; the other files can go together in one \`file_paths\` call.
