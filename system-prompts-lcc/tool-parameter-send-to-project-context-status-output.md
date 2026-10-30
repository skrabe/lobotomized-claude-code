<!--
name: 'Tool parameter: Send to project context status result field'
description: >-
  outputSchema describe() on the send-to-project context reader's status enum
  explaining delivered, already_delivered, nothing_read and no_run.
ccVersion: 2.1.314
-->
delivered: context holds what the command read. already_delivered: an earlier call in this run returned it. nothing_read: the run sends one message and read no context. no_run: no /send-to-project run of the user’s waits in this turn.
