<!--
name: Artifact Claude Docs Existing Document
description: >-
  Tells the model an Artifact already binds a Claude Docs project and how to
  read/write it instead of creating another.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_EXISTING_DOCUMENT_VAR_0
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_EXISTING_DOCUMENT_VAR_1
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_EXISTING_DOCUMENT_VAR_2
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_EXISTING_DOCUMENT_VAR_3
-->
Its content is a Claude Docs document that already exists; its Claude Docs id is this Artifact's own id, ${TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_EXISTING_DOCUMENT_VAR_0}. Read it once with the Claude Docs connector (\`read\`, ref {"object":"project","id":${TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_EXISTING_DOCUMENT_VAR_0}}) for its tab and root-node ids, then write into it (\`batch\` / \`update\`, ${TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_EXISTING_DOCUMENT_VAR_1(TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_EXISTING_DOCUMENT_VAR_2)})${TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_EXISTING_DOCUMENT_VAR_3?" as the instructions below describe":""} — do not create another; only if Claude Docs says there is no such document${TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_EXISTING_DOCUMENT_VAR_3?", bind one as those instructions describe":" does it need one created and bound to this Artifact"}. Nothing is published to this URL for its content
