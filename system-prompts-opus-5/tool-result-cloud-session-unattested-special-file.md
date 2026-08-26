<!--
name: 'Tool Result: Cloud Session Unattested Special File'
description: >-
  Remote-file refusal when the path is a special file on the served machine and
  approvals for calls to that machine are not attested.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_CLOUD_SESSION_UNATTESTED_SPECIAL_FILE_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_UNATTESTED_SPECIAL_FILE_VAR_1
  - TOOL_RESULT_CLOUD_SESSION_UNATTESTED_SPECIAL_FILE_VAR_2
  - TOOL_RESULT_CLOUD_SESSION_UNATTESTED_SPECIAL_FILE_VAR_3
-->
${TOOL_RESULT_CLOUD_SESSION_UNATTESTED_SPECIAL_FILE_VAR_0} can't be ${TOOL_RESULT_CLOUD_SESSION_UNATTESTED_SPECIAL_FILE_VAR_1==="read"?"read":"changed"} from a cloud session yet: it is ${TOOL_RESULT_CLOUD_SESSION_UNATTESTED_SPECIAL_FILE_VAR_2} on this machine, which its file tools do not serve until approvals for calls to this machine are attested. Use ${TOOL_RESULT_CLOUD_SESSION_UNATTESTED_SPECIAL_FILE_VAR_3} there if its sandbox allows, or ask the user.
