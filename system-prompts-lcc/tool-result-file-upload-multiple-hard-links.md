<!--
name: 'Tool Result: file_upload Blocked By Multiple Hard Links'
description: >-
  Rejection returned by jiy when an upload target has nlink>1 (e.g. node_modules
  stores that Bun/pnpm hard-link), explaining the aliasing risk and telling the
  model to copy the file and upload the copy; delivered as a <tool_use_error>
  tool_result.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_FILE_UPLOAD_MULTIPLE_HARD_LINKS_VAR_0
-->
Cannot upload "${TOOL_RESULT_FILE_UPLOAD_MULTIPLE_HARD_LINKS_VAR_0}": the file has multiple hard links, which can alias a file outside the session's allowed directories. Copy the file and upload the copy.
