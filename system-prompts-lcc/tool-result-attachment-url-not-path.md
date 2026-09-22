<!--
name: Attachment is a URL not a path
description: >-
  SendMessage attachment validation error returned to the model when a path
  looks like a URL.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_ATTACHMENT_URL_NOT_PATH_VAR_0
-->
Attachment "${TOOL_RESULT_ATTACHMENT_URL_NOT_PATH_VAR_0}" looks like a URL, not a local file path. This tool can only send files that exist on the local filesystem — download or write the content to a local file first, then pass that path.
