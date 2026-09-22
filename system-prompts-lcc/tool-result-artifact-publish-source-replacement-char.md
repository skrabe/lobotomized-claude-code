<!--
name: Artifact Publish Source Replacement Character
description: >-
  Publish tool error when the source file contains U+FFFD and must be rewritten
  as UTF-8 before publishing.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_REPLACEMENT_CHAR_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_REPLACEMENT_CHAR_VAR_1
-->
file_path: the source file has the replacement character U+FFFD at ${TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_REPLACEMENT_CHAR_VAR_0}, usually left where an earlier edit or paste lost a character. Replace it with the intended text (in HTML, write an intended U+FFFD as &#xFFFD;), ${TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_REPLACEMENT_CHAR_VAR_1}
