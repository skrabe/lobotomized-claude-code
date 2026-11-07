<!--
name: 'Tool Result: MCP connector file background-job remedy with read block'
description: >-
  Remedy in the background-job connector file refusal, under the
  read-outside-working-directories block, telling the user to ask from a session
  without a background job
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_BLOCK_READS_REMEDY_VAR_0
-->
This session also blocks reads outside its working directories (permissions.blockReadsOutsideWorkingDirectories), so an attached file is sent only if that setting lets the ${TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_BLOCK_READS_REMEDY_VAR_0} tool read it. To send this file, the user can ask in a session that runs no background job, which can send a file that is in the folder it was started in or in a folder added for it (--add-dir, or /add-dir with "Yes, for this session", or a folder allowed on a prompt), if that session may read it.
