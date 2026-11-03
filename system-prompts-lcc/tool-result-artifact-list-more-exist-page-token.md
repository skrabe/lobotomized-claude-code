<!--
name: 'Tool result: Artifact list more exist page token'
description: >-
  Artifact listing suffix saying more artifacts exist and giving the page_token
  to pass with the same scope for the next page.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_ARTIFACT_LIST_MORE_EXIST_PAGE_TOKEN_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_MORE_EXIST_PAGE_TOKEN_VAR_1
-->

(More exist: pass \`page_token\` "${TOOL_RESULT_ARTIFACT_LIST_MORE_EXIST_PAGE_TOKEN_VAR_0}" with the same \`scope\` to list the next ones.${TOOL_RESULT_ARTIFACT_LIST_MORE_EXIST_PAGE_TOKEN_VAR_1.scope===void 0?"":" Artifacts shared from another organization come with the last page."})
