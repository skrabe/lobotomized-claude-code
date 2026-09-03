<!--
name: 'Tool Result: Remote Host Still Running'
description: >-
  still_running tool_result when the host reports the command is still under
  way, telling the model not to re-run it.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_HOST_STILL_RUNNING_VAR_0
  - TOOL_RESULT_REMOTE_HOST_STILL_RUNNING_VAR_1
-->
${TOOL_RESULT_REMOTE_HOST_STILL_RUNNING_VAR_0}${TOOL_RESULT_REMOTE_HOST_STILL_RUNNING_VAR_1==="unasked"?"":" the command is STILL RUNNING there"}; its outcome is not known yet. Do not re-run it — check on its effect later, or ask the user.
