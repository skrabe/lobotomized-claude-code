<!--
name: Start task supplied file ids refused
description: >-
  Requires local paths instead of file ids and explains why old approvals cannot
  be reused.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_START_TASK_FILE_IDS_REFUSED_VAR_0
  - TOOL_RESULT_START_TASK_FILE_IDS_REFUSED_VAR_1
  - TOOL_RESULT_START_TASK_FILE_IDS_REFUSED_VAR_2
  - TOOL_RESULT_START_TASK_FILE_IDS_REFUSED_VAR_3
-->
${TOOL_RESULT_START_TASK_FILE_IDS_REFUSED_VAR_0} file entries must give a \`${TOOL_RESULT_START_TASK_FILE_IDS_REFUSED_VAR_1}\`; this client uploads the file and fills in the ${TOOL_RESULT_START_TASK_FILE_IDS_REFUSED_VAR_2} itself. If these ${TOOL_RESULT_START_TASK_FILE_IDS_REFUSED_VAR_2}s came from an approval given before Claude Code restarted, that approval cannot be reused: call ${TOOL_RESULT_START_TASK_FILE_IDS_REFUSED_VAR_0} again with paths. ${TOOL_RESULT_START_TASK_FILE_IDS_REFUSED_VAR_3}
