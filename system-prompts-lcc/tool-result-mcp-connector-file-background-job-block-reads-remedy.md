<!--
name: 'Tool Result: MCP connector file background-job remedy with read block'
description: >-
  Remedy in the background-job connector file refusal, under the
  read-outside-working-directories block, telling the user to run Claude Code in
  a terminal with no background job.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_BLOCK_READS_REMEDY_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_BLOCK_READS_REMEDY_VAR_1
-->
This session also blocks reads outside its working directories (${TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_BLOCK_READS_REMEDY_VAR_0}), so an attached file is sent only if ${TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_BLOCK_READS_REMEDY_VAR_0.includes(" and ")?"those settings let":"that setting lets"} the ${TOOL_RESULT_MCP_CONNECTOR_FILE_BACKGROUND_JOB_BLOCK_READS_REMEDY_VAR_1} tool read it. To send this file, the user can run Claude Code in a terminal, with no background job, and ask there.
