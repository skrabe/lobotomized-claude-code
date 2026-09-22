<!--
name: Bundle Upload Credential Previous Way Error
description: >-
  Agent-tool error when a hardened bundle upload still fails on uncommitted
  credentials, telling the model the previous upload path keeps nothing back
  either.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_BUNDLE_UPLOAD_CREDENTIAL_PREVIOUS_WAY_ERROR_VAR_0
  - TOOL_RESULT_BUNDLE_UPLOAD_CREDENTIAL_PREVIOUS_WAY_ERROR_VAR_1
-->
${TOOL_RESULT_BUNDLE_UPLOAD_CREDENTIAL_PREVIOUS_WAY_ERROR_VAR_0.error} ${TOOL_RESULT_BUNDLE_UPLOAD_CREDENTIAL_PREVIOUS_WAY_ERROR_VAR_1.error.replace(/^Not uploading this working tree: /,"It is not uploaded the previous way either (that way keeps nothing back): ")}
