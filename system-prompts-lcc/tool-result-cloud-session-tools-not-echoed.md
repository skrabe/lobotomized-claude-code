<!--
name: 'Tool Result: Cloud Session Tools Not Echoed'
description: >-
  Cloud-session creation failure when the service did not echo back the
  requested --tools list; the session is archived and the user is told to use
  --disallowed-tools.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_CLOUD_SESSION_TOOLS_NOT_ECHOED_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_TOOLS_NOT_ECHOED_VAR_1
  - TOOL_RESULT_CLOUD_SESSION_TOOLS_NOT_ECHOED_VAR_2
  - TOOL_RESULT_CLOUD_SESSION_TOOLS_NOT_ECHOED_VAR_3
-->
The cloud session could not be limited to the tools you asked for (--tools ${TOOL_RESULT_CLOUD_SESSION_TOOLS_NOT_ECHOED_VAR_0(TOOL_RESULT_CLOUD_SESSION_TOOLS_NOT_ECHOED_VAR_1,",")}) because ${TOOL_RESULT_CLOUD_SESSION_TOOLS_NOT_ECHOED_VAR_2}. ${TOOL_RESULT_CLOUD_SESSION_TOOLS_NOT_ECHOED_VAR_3} Keep tools out with --disallowed-tools instead.
