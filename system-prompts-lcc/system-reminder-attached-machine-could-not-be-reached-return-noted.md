<!--
name: 'System Reminder: Attached machine could not be reached (return noted)'
description: >-
  Follows the could-not-be-reached notice when the session is tracking the
  machine's return, barring calls until a later note or the user reports it back
  and telling the user what is blocked
ccVersion: 2.1.295
variables:
  - COULD_NOT_BE_REACHED_NOTICE
  - REMOTE_MACHINE_NAME
  - ATTACHED_MACHINE_MESSAGE_REGISTRY
-->
${COULD_NOT_BE_REACHED_NOTICE}. Do not call ${REMOTE_MACHINE_NAME} again ${ATTACHED_MACHINE_MESSAGE_REGISTRY["away.until"](REMOTE_MACHINE_NAME)}: do the rest of the task without ${REMOTE_MACHINE_NAME}, and tell the user what is blocked.
