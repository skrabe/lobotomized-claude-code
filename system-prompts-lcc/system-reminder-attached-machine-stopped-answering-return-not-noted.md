<!--
name: 'System Reminder: Attached machine stopped answering (return not noted)'
description: >-
  Follows the stopped-answering notice when the session is not tracking the
  machine's return, forbidding retries of non-idempotent commands until
  reconnection and further calls this turn, and allowing one recheck only when
  the user says it is…
ccVersion: 2.1.295
variables:
  - STOPPED_ANSWERING_NOTICE
  - REMOTE_MACHINE_NAME
  - ATTACHED_MACHINE_MESSAGE_REGISTRY
-->
${STOPPED_ANSWERING_NOTICE} Do not retry non-idempotent commands on ${REMOTE_MACHINE_NAME} until ${REMOTE_MACHINE_NAME} reconnects, and do not call it again ${ATTACHED_MACHINE_MESSAGE_REGISTRY["away.until"]()}: do the rest of the task without ${REMOTE_MACHINE_NAME}, and tell the user what is blocked and what you could not verify. ${ATTACHED_MACHINE_MESSAGE_REGISTRY["away.ending"]()}
