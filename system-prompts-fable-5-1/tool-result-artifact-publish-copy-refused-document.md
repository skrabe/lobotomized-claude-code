<!--
name: 'Tool Result: Artifact Publish Copy Refused Document'
description: >-
  Publish abort telling the model a copied page/SVG/XML cannot skip this tool's
  checks and nothing was published.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_DOCUMENT_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_DOCUMENT_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_DOCUMENT_VAR_2
-->
copied file ${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_DOCUMENT_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_DOCUMENT_VAR_1[0].c.path)} is ${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_DOCUMENT_VAR_1[0].contentType}: a page, SVG or XML document cannot be copied from another artifact into a publish (its content must pass this tool's checks, which a server-side copy skips) — read it with action "read_file" and publish it from the local copy instead. Nothing was published.${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_DOCUMENT_VAR_2}
