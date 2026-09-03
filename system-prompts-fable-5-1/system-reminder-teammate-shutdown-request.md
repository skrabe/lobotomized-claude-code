<!--
name: Teammate Shutdown Request
description: >-
  Appends shutdown-approval instructions onto a teammate mailbox
  shutdown_request before it is passed to the model.
ccVersion: 2.1.257
variables:
  - SYSTEM_REMINDER_TEAMMATE_SHUTDOWN_REQUEST_VAR_0
  - SYSTEM_REMINDER_TEAMMATE_SHUTDOWN_REQUEST_VAR_1
  - SYSTEM_REMINDER_TEAMMATE_SHUTDOWN_REQUEST_VAR_2
-->
${SYSTEM_REMINDER_TEAMMATE_SHUTDOWN_REQUEST_VAR_0}

This is a shutdown request. ${SYSTEM_REMINDER_TEAMMATE_SHUTDOWN_REQUEST_VAR_1(SYSTEM_REMINDER_TEAMMATE_SHUTDOWN_REQUEST_VAR_2.requestId)}
