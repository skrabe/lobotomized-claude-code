<!--
name: 'Tool Result: Remote Host Disconnected During Call'
description: >-
  dropped tool_result when the host disconnected mid-call, telling the model not
  to re-run until it checks whether the command took effect.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_HOST_DISCONNECTED_DURING_CALL_VAR_0
-->
${TOOL_RESULT_REMOTE_HOST_DISCONNECTED_DURING_CALL_VAR_0} disconnected during the call. If the command had started, it has most likely continued to run there, but its result could not be delivered. Do not simply re-run it — first check whether it took effect (e.g. whether the file, commit or process now exists) or ask the user.
