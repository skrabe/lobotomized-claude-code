<!--
name: 'Tool Result: Remote Host Unresponsive'
description: >-
  Remote-host tool_result when the attached machine stopped answering health
  checks, telling the model not to retry non-idempotent commands.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_0
  - TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_1
  - TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_2
  - TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_3
  - TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_4
-->
${TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_0} stopped answering ${TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_1?"while this command was running":"after this command was sent to it"} (${TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_2} checks about ${TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_3.round(TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_4/1000)} s apart went unanswered). Its state is unknown — it may have completed, failed, ${TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_1?"or still be running":"never started, or still be running"}. Do not retry non-idempotent commands on ${TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_0} until ${TOOL_RESULT_REMOTE_HOST_UNRESPONSIVE_VAR_0} reconnects; continue with work that doesn't need it and say what you could not verify.
