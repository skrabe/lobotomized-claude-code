<!--
name: Team Shutdown Request Approve
description: >-
  Instructions appended onto a teammate shutdown_request so the model can
  approve or decline via SendMessage.
ccVersion: 2.1.257
variables:
  - SYSTEM_REMINDER_TEAM_SHUTDOWN_REQUEST_APPROVE_VAR_0
  - SYSTEM_REMINDER_TEAM_SHUTDOWN_REQUEST_APPROVE_VAR_1
  - SYSTEM_REMINDER_TEAM_SHUTDOWN_REQUEST_APPROVE_VAR_2
-->
To approve it, call ${SYSTEM_REMINDER_TEAM_SHUTDOWN_REQUEST_APPROVE_VAR_0} with exactly this input, where "message" is a JSON object rather than a string${SYSTEM_REMINDER_TEAM_SHUTDOWN_REQUEST_APPROVE_VAR_1?"":" and request_id is the request's requestId value, copied verbatim"}: ${SYSTEM_REMINDER_TEAM_SHUTDOWN_REQUEST_APPROVE_VAR_2}. Approving ends your process; a plain-text acknowledgment does not shut you down. To decline, for example because you're mid-task, send the same input with "approve": false and a "reason".
