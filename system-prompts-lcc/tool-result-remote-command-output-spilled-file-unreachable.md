<!--
name: 'Tool Result: remote command''s spilled output file unreachable'
description: >-
  Placeholder text substituted for a path in remote command output that points
  to a spilled file this session cannot read, suggesting re-running with
  head/tail/grep on the remote machine if safe
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_REMOTE_COMMAND_OUTPUT_SPILLED_FILE_UNREACHABLE_VAR_0
  - TOOL_RESULT_REMOTE_COMMAND_OUTPUT_SPILLED_FILE_UNREACHABLE_VAR_1
  - TOOL_RESULT_REMOTE_COMMAND_OUTPUT_SPILLED_FILE_UNREACHABLE_VAR_2
-->
a file on ${TOOL_RESULT_REMOTE_COMMAND_OUTPUT_SPILLED_FILE_UNREACHABLE_VAR_0} that cannot be read from here — the command already ran on ${TOOL_RESULT_REMOTE_COMMAND_OUTPUT_SPILLED_FILE_UNREACHABLE_VAR_0}, so only this part of its output is out of reach. If it is safe to repeat, re-run it there with ${TOOL_RESULT_REMOTE_COMMAND_OUTPUT_SPILLED_FILE_UNREACHABLE_VAR_1(TOOL_RESULT_REMOTE_COMMAND_OUTPUT_SPILLED_FILE_UNREACHABLE_VAR_2)} to see the part you need
