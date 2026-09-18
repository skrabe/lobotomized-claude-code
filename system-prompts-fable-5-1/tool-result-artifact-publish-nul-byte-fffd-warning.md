<!--
name: Artifact Publish Nul Byte Fffd Warning
description: >-
  Publish tool_result warning when published content contains a NUL byte that
  browsers turn into U+FFFD, which can break scripts.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_NUL_BYTE_FFFD_WARNING_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_NUL_BYTE_FFFD_WARNING_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_NUL_BYTE_FFFD_WARNING_VAR_2
-->
${TOOL_RESULT_ARTIFACT_PUBLISH_NUL_BYTE_FFFD_WARNING_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_NUL_BYTE_FFFD_WARNING_VAR_1)} contains a NUL (\\u0000) byte at ${TOOL_RESULT_ARTIFACT_PUBLISH_NUL_BYTE_FFFD_WARNING_VAR_2}: it was published, but browsers turn that byte into U+FFFD (�), and in script code outside a string literal that is a syntax error that stops the whole script — remove it (or write the escape \\u0000 if the character is meant) and publish again.
