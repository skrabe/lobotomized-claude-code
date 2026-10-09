<!--
name: 'System Reminder: Attached machine could not be reached (return not noted)'
description: >-
  Follows the could-not-be-reached notice when the session is not tracking the
  machine's return, adding that an oversized call will not succeed on retry,
  barring calls this turn, and allowing one recheck only when the user says it
  is back
ccVersion: 2.1.295
variables:
  - COULD_NOT_BE_REACHED_NOTICE
  - REMOTE_MACHINE_NAME
  - ATTACHED_MACHINE_MESSAGE_REGISTRY
-->
${COULD_NOT_BE_REACHED_NOTICE}; a call that was too large to deliver will not succeed on a retry. Do not call ${REMOTE_MACHINE_NAME} again ${ATTACHED_MACHINE_MESSAGE_REGISTRY["away.until"]()}: do the rest of the task without ${REMOTE_MACHINE_NAME}, and tell the user what is blocked. ${ATTACHED_MACHINE_MESSAGE_REGISTRY["away.ending"]()}
