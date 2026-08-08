<!--
name: Artifact Reply Text Over Byte Limit
description: >-
  validateInput failure (errorCode 11) reporting the reply's UTF-8 byte size
  against the limit and telling Claude to shorten it.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_ARTIFACT_REPLY_TEXT_TOO_LARGE_VAR_0
  - TOOL_RESULT_ARTIFACT_REPLY_TEXT_TOO_LARGE_VAR_1
-->

text is ${TOOL_RESULT_ARTIFACT_REPLY_TEXT_TOO_LARGE_VAR_0} bytes of UTF-8 — the limit is ${TOOL_RESULT_ARTIFACT_REPLY_TEXT_TOO_LARGE_VAR_1}.
