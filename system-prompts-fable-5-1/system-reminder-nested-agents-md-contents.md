<!--
name: 'System Reminder: Nested AGENTS.md contents'
description: >-
  Attaches a nested AGENTS.md file's contents to a Read tool result when the
  agents-md plugin finds instruction files below the session's working directory
ccVersion: 2.1.274
variables:
  - INSTRUCTION_FILE_PATH_FN
  - INSTRUCTION_FILE
-->
Contents of ${INSTRUCTION_FILE_PATH_FN(INSTRUCTION_FILE)}:

${INSTRUCTION_FILE.content.trim()}
