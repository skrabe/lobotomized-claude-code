<!--
name: 'System Reminder: Large file full-content reading guidance'
description: >-
  Advises how to read full large-file content for analysis, preferably inside a
  subagent when the Agent tool is available
ccVersion: 2.1.178
variables:
  - FULL_CONTENT_READING_INSTRUCTION
  - AGENT_TOOL_NAME
  - SUBAGENT_READING_INSTRUCTION_EXAMPLE
-->
- To read the full content for analysis or summary: ${FULL_CONTENT_READING_INSTRUCTION}
- If ${AGENT_TOOL_NAME} is available, do this in a subagent so the full output stays out of your context. Pass the instruction above verbatim and state exactly what it must return (e.g. "${SUBAGENT_READING_INSTRUCTION_EXAMPLE}"); a vague "summarize this" loses detail.
