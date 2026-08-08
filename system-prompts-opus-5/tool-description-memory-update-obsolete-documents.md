<!--
name: 'Tool Description: Update or obsolete memory documents'
description: >-
  Bullet in the memory_write prompt telling the model how to rewrite
  wrong/outdated memories and how to retire a document plus its index entry.
ccVersion: 2.1.224
variables:
  - TOOL_DESCRIPTION_MEMORY_UPDATE_OBSOLETE_DOCUMENTS_VAR_0
-->
- Update memories that turn out to be wrong or outdated by rewriting the document with ${TOOL_DESCRIPTION_MEMORY_UPDATE_OBSOLETE_DOCUMENTS_VAR_0}; when nothing in a document is worth keeping, replace its content with a one-line note saying it is obsolete and remove its entry from the index
