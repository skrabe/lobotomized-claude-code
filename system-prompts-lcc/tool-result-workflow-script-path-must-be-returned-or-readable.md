<!--
name: Workflow Script Path Must Be Returned Or Readable
description: >-
  Workflow tool validation error when scriptPath is not a prior tool result path
  or an already-readable file.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_WORKFLOW_SCRIPT_PATH_MUST_BE_RETURNED_OR_READABLE_VAR_0
  - TOOL_RESULT_WORKFLOW_SCRIPT_PATH_MUST_BE_RETURNED_OR_READABLE_VAR_1
  - TOOL_RESULT_WORKFLOW_SCRIPT_PATH_MUST_BE_RETURNED_OR_READABLE_VAR_2
-->
scriptPath must be a script path this tool returned, or a file you can already read (the working directory or a directory you have added): ${TOOL_RESULT_WORKFLOW_SCRIPT_PATH_MUST_BE_RETURNED_OR_READABLE_VAR_0}
A session that cannot call ${TOOL_RESULT_WORKFLOW_SCRIPT_PATH_MUST_BE_RETURNED_OR_READABLE_VAR_1} cannot load any scriptPath. Pass the whole script inline through ${TOOL_RESULT_WORKFLOW_SCRIPT_PATH_MUST_BE_RETURNED_OR_READABLE_VAR_2}'s \`script\` input instead.
