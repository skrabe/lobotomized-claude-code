<!--
name: 'Tool Result: Cloud Session First Prompt Not Sent'
description: >-
  Cloud-session creation failure when the service accepted the requested tools
  but the first prompt could not be delivered.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_CLOUD_SESSION_FIRST_PROMPT_NOT_SENT_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_FIRST_PROMPT_NOT_SENT_VAR_1
  - TOOL_RESULT_CLOUD_SESSION_FIRST_PROMPT_NOT_SENT_VAR_2
-->
The service accepted the list of tools you asked for, but ${{busy:`was busy or could not be reached while your prompt was being sent${TOOL_RESULT_CLOUD_SESSION_FIRST_PROMPT_NOT_SENT_VAR_0}. ${TOOL_RESULT_CLOUD_SESSION_FIRST_PROMPT_NOT_SENT_VAR_1}; run the command again in a moment.`,refused:`refused your prompt${TOOL_RESULT_CLOUD_SESSION_FIRST_PROMPT_NOT_SENT_VAR_0}. ${TOOL_RESULT_CLOUD_SESSION_FIRST_PROMPT_NOT_SENT_VAR_1}.${TOOL_RESULT_CLOUD_SESSION_FIRST_PROMPT_NOT_SENT_VAR_2}`,unsent:`your prompt could not be sent from this machine${TOOL_RESULT_CLOUD_SESSION_FIRST_PROMPT_NOT_SENT_VAR_0}. ${TOOL_RESULT_CLOUD_SESSION_FIRST_PROMPT_NOT_SENT_VAR_1}.${TOOL_RESULT_CLOUD_SESSION_FIRST_PROMPT_NOT_SENT_VAR_2}`}[e.kind]}
