<!--
name: 'Tool Result: Artifact DB page-only document'
description: >-
  Write refused because the document is kept by the artifact's own page;
  read-only via read_db, don't retry
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_ARTIFACT_DB_PAGE_ONLY_DOCUMENT_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_PAGE_ONLY_DOCUMENT_VAR_1
-->
${TOOL_RESULT_ARTIFACT_DB_PAGE_ONLY_DOCUMENT_VAR_0} is kept by the artifact's own page. You can read it with read_db, but not write or delete it. Trying again will not help, so do not try to write it another way or under another name.${TOOL_RESULT_ARTIFACT_DB_PAGE_ONLY_DOCUMENT_VAR_1?" The batch's other writes can be sent again without that one.":""} If the task can be done by changing the artifact's other content, do that; if not, ask the user to change this document on the artifact's page
