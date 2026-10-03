<!--
name: Files not delivered instruction
description: >-
  Fragment of the file-delivery tool result instructing the model to tell the
  user which files were not delivered and why, followed by the temporary-failure
  retry hint.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_FILES_NOT_DELIVERED_INSTRUCTION_VAR_0
  - TOOL_RESULT_FILES_NOT_DELIVERED_INSTRUCTION_VAR_1
  - TOOL_RESULT_FILES_NOT_DELIVERED_INSTRUCTION_VAR_2
-->

Tell the user the ${TOOL_RESULT_FILES_NOT_DELIVERED_INSTRUCTION_VAR_0(TOOL_RESULT_FILES_NOT_DELIVERED_INSTRUCTION_VAR_1.length,"file was","files were")} not delivered and why.${TOOL_RESULT_FILES_NOT_DELIVERED_INSTRUCTION_VAR_2(TOOL_RESULT_FILES_NOT_DELIVERED_INSTRUCTION_VAR_1)}
