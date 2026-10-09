<!--
name: 'System Reminder: Attached machine stopped answering (return noted)'
description: >-
  Follows the stopped-answering notice when the session is tracking the
  machine's return, barring calls until a later note or the user reports it
  back, requiring a check of what the command did before repeating it, and
  telling the user what i…
ccVersion: 2.1.295
variables:
  - STOPPED_ANSWERING_NOTICE
  - REMOTE_MACHINE_NAME
  - ATTACHED_MACHINE_MESSAGE_REGISTRY
-->
${STOPPED_ANSWERING_NOTICE} Do not call ${REMOTE_MACHINE_NAME} again ${ATTACHED_MACHINE_MESSAGE_REGISTRY["away.until"](REMOTE_MACHINE_NAME)}; then check what this command did before repeating it. Meanwhile do the rest of the task without ${REMOTE_MACHINE_NAME}, and tell the user what is blocked and what you could not verify.
