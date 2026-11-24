<!--
name: 'Tool Result: Served Tool Ask Directory Unusable'
description: >-
  Served-tool refusal when the directory where the call asked for permission is
  unknown, outside the start directory, or gone; tells the model to check and
  resend.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_SERVED_TOOL_ASK_DIRECTORY_UNUSABLE_VAR_0
  - TOOL_RESULT_SERVED_TOOL_ASK_DIRECTORY_UNUSABLE_VAR_1
  - TOOL_RESULT_SERVED_TOOL_ASK_DIRECTORY_UNUSABLE_VAR_2
-->
${TOOL_RESULT_SERVED_TOOL_ASK_DIRECTORY_UNUSABLE_VAR_0} was not run: the directory where it asked for permission ${TOOL_RESULT_SERVED_TOOL_ASK_DIRECTORY_UNUSABLE_VAR_1===void 0?"is not known, or is outside the directory where this session's tools started":"is gone (deleted, moved, replaced by a link, or unreadable)"}. A new call starts where the shell stands now, and may need approval again. Check that it still does what you mean there, then send it again.${TOOL_RESULT_SERVED_TOOL_ASK_DIRECTORY_UNUSABLE_VAR_1===void 0?"":TOOL_RESULT_SERVED_TOOL_ASK_DIRECTORY_UNUSABLE_VAR_2(TOOL_RESULT_SERVED_TOOL_ASK_DIRECTORY_UNUSABLE_VAR_1)}
