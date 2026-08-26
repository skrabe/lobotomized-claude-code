<!--
name: 'Tool Result: Remote Host Not Served — Omit Local'
description: >-
  not_served tool_result when the named machine does not serve the tool, telling
  the model to omit the host qualifier and run it locally.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_HOST_NOT_SERVED_OMIT_LOCAL_VAR_0
  - TOOL_RESULT_REMOTE_HOST_NOT_SERVED_OMIT_LOCAL_VAR_1
  - TOOL_RESULT_REMOTE_HOST_NOT_SERVED_OMIT_LOCAL_VAR_2
  - TOOL_RESULT_REMOTE_HOST_NOT_SERVED_OMIT_LOCAL_VAR_3
-->
${TOOL_RESULT_REMOTE_HOST_NOT_SERVED_OMIT_LOCAL_VAR_0} does not serve ${TOOL_RESULT_REMOTE_HOST_NOT_SERVED_OMIT_LOCAL_VAR_1} right now; omit "${TOOL_RESULT_REMOTE_HOST_NOT_SERVED_OMIT_LOCAL_VAR_2}" to run it ${TOOL_RESULT_REMOTE_HOST_NOT_SERVED_OMIT_LOCAL_VAR_3()}.
