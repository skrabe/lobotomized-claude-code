<!--
name: 'Auto mode: no verdict, call not judged as run'
description: >-
  Auto-mode deny message when the check reviewed a call without knowing what it
  runs as.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_JUDGED_AS_RUN_VAR_0
  - TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_JUDGED_AS_RUN_VAR_1
  - TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_JUDGED_AS_RUN_VAR_2
-->
${TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_JUDGED_AS_RUN_VAR_0} gave no verdict for ${TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_JUDGED_AS_RUN_VAR_1}: it reviewed your ${TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_JUDGED_AS_RUN_VAR_2} call, which runs as ${TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_JUDGED_AS_RUN_VAR_1}, without knowing that. This is not a judgment that the action is unsafe. Call ${TOOL_RESULT_AUTO_MODE_NO_VERDICT_NOT_JUDGED_AS_RUN_VAR_1} itself, with \`message\`, each option as an argument of its own, and the target as \`session_id\` (none for a lookup by title), so that auto mode reviews it.
