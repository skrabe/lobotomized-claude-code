<!--
name: Artifact Read Summary Html Persist Failed
description: Artifact-read summary result when saving the raw HTML to disk failed.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_READ_SUMMARY_HTML_PERSIST_FAILED_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_SUMMARY_HTML_PERSIST_FAILED_VAR_1
-->
saving the raw HTML to disk failed${TOOL_RESULT_ARTIFACT_READ_SUMMARY_HTML_PERSIST_FAILED_VAR_0&&TOOL_RESULT_ARTIFACT_READ_SUMMARY_HTML_PERSIST_FAILED_VAR_1?" — this summary cannot be republished from; a publish to this artifact will try to hand you its full source first, and if saving to disk keeps failing here, tell the user":""}
