<!--
name: 'Tool Result: Artifact Publish Source Undecodable'
description: >-
  Publish error when the source file is not valid UTF-8/UTF-16 text, asking the
  model to rewrite it as UTF-8 and republish.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_UNDECODABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_UNDECODABLE_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_UNDECODABLE_VAR_2
-->
file_path: the source file is not valid ${TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_UNDECODABLE_VAR_0==="utf-16le"?"UTF-16":"UTF-8"} text (first invalid byte at ${TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_UNDECODABLE_VAR_1}). It may be saved in another encoding or contain binary data. Rewrite it as UTF-8, ${TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_UNDECODABLE_VAR_2}
