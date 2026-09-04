<!--
name: Artifact Publish Copy Script Without Script Extension
description: >-
  Tool result when a copied script is stored under a non-script name so a
  type-created artifact would treat it as data.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_SCRIPT_WITHOUT_SCRIPT_EXTENSION_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_SCRIPT_WITHOUT_SCRIPT_EXTENSION_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_SCRIPT_WITHOUT_SCRIPT_EXTENSION_VAR_2
-->
copied file ${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_SCRIPT_WITHOUT_SCRIPT_EXTENSION_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_COPY_SCRIPT_WITHOUT_SCRIPT_EXTENSION_VAR_1.c.path)} is ${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_SCRIPT_WITHOUT_SCRIPT_EXTENSION_VAR_1.contentType}: a script its source stores under a name that does not say so cannot be copied into an artifact made from a type (the approval counted it as data) — copy it to a path with a script extension, or read it with action "read_file" and publish it from the local copy instead. Nothing was published.${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_SCRIPT_WITHOUT_SCRIPT_EXTENSION_VAR_2}
