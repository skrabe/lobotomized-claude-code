<!--
name: Project write retry existing document
description: >-
  Advises retrying a transient save failure while retaining the existing
  document.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_PROJECT_WRITE_RETRY_EXISTING_DOCUMENT_VAR_0
  - TOOL_RESULT_PROJECT_WRITE_RETRY_EXISTING_DOCUMENT_VAR_1
-->
 ${TOOL_RESULT_PROJECT_WRITE_RETRY_EXISTING_DOCUMENT_VAR_0} ${TOOL_RESULT_PROJECT_WRITE_RETRY_EXISTING_DOCUMENT_VAR_1} Try the same project_write again, up to two retries in total. If it still fails, tell the user that the new content was not saved, and offer it to them another way.
