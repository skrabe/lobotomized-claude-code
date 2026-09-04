<!--
name: Artifact read summary raw HTML persist failed
description: >-
  Header clause in a summarized artifact read stating that saving the raw HTML
  to disk failed.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_READ_SUMMARY_HTML_PERSIST_FAILED_VAR_0
-->
saving the raw HTML to disk failed${TOOL_RESULT_ARTIFACT_READ_SUMMARY_HTML_PERSIST_FAILED_VAR_0&&TOOL_RESULT_ARTIFACT_READ_SUMMARY_HTML_PERSIST_FAILED_VAR_1?" — this summary cannot be republished from; a publish to this artifact will try to hand you its full source first, and if saving to disk keeps failing here, tell the user":""}
