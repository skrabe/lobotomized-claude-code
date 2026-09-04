<!--
name: Artifact Publish Copy Refused
description: >-
  Tool result when staging a copied file from another artifact is refused, with
  a not-found hint when the status text matches.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_2
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_3
-->
copying ${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_1.path)} from artifact ${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_1.from.slug} (${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_1.from.path)}) was refused (${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_2.status}: ${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_3})${/not found/.test(TOOL_RESULT_ARTIFACT_PUBLISH_COPY_REFUSED_VAR_3)?" — a source Artifact that does not exist, that this account cannot open, or that is in another organization all answer alike":""}
