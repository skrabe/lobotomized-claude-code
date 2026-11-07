<!--
name: 'Tool Result: MCP connector file block-reads-outside clause'
description: >-
  Clause in the connector file-path refusal saying
  permissions.blockReadsOutsideWorkingDirectories limits sending files from the
  attachments and outputs folders to what the read tool may read
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_BLOCK_READS_OUTSIDE_CLAUSE_VAR_0
-->
 This session also blocks reads outside its working directories (permissions.blockReadsOutsideWorkingDirectories): a file in one of the folders kept for attachments and outputs is sent only if that setting lets the ${TOOL_RESULT_MCP_CONNECTOR_FILE_BLOCK_READS_OUTSIDE_CLAUSE_VAR_0} tool read it.
