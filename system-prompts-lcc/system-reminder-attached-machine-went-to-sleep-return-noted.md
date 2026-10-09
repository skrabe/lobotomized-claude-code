<!--
name: 'System Reminder: Attached machine went to sleep (return noted)'
description: >-
  Follows the went-to-sleep notice when the session is tracking the machine's
  return, barring calls until a later note or the user reports it back, then
  requiring a check of what the command did and telling the user what is paused
ccVersion: 2.1.295
variables:
  - WENT_TO_SLEEP_NOTICE
  - REMOTE_MACHINE_NAME
-->
${WENT_TO_SLEEP_NOTICE} Do not call ${REMOTE_MACHINE_NAME} again until a later attached-machines note says ${REMOTE_MACHINE_NAME} is reachable again, or the user says it is back or asks you to try again; then check what this command did before sending anything else to ${REMOTE_MACHINE_NAME}. Meanwhile do the rest of the task without ${REMOTE_MACHINE_NAME}, and tell the user what is paused.
