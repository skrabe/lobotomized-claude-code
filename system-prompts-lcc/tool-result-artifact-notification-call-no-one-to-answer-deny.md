<!--
name: 'Tool Result: Artifact Notification Call No One To Answer Deny'
description: >-
  checkPermissions deny for an artifact call needing a yes when no one can
  answer: in Cowork on a turn not started by the user, or in plan mode. It tells
  the model to raise it in chat and not retry.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_ARTIFACT_NOTIFICATION_CALL_NO_ONE_TO_ANSWER_DENY_VAR_0
  - TOOL_RESULT_ARTIFACT_NOTIFICATION_CALL_NO_ONE_TO_ANSWER_DENY_VAR_1
  - TOOL_RESULT_ARTIFACT_NOTIFICATION_CALL_NO_ONE_TO_ANSWER_DENY_VAR_2
-->
${TOOL_RESULT_ARTIFACT_NOTIFICATION_CALL_NO_ONE_TO_ANSWER_DENY_VAR_0}. This needs a yes to: ${TOOL_RESULT_ARTIFACT_NOTIFICATION_CALL_NO_ONE_TO_ANSWER_DENY_VAR_1} ${TOOL_RESULT_ARTIFACT_NOTIFICATION_CALL_NO_ONE_TO_ANSWER_DENY_VAR_2?"No one can answer that prompt in this Cowork session, and this turn was not started by the user's own message — tell the user in chat; do not retry it on this turn.":"No one can answer that prompt from plan mode in this session — keep planning in the plan file and raise it with the user in chat; do not retry while plan mode is on."}
