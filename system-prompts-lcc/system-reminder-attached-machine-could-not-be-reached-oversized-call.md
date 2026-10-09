<!--
name: 'System Reminder: Attached machine could not be reached (oversized call)'
description: >-
  Appends to the could-not-be-reached notice that a call too large to deliver
  will not succeed on a retry, when the failure is on this session's side rather
  than the machine not answering
ccVersion: 2.1.295
variables:
  - COULD_NOT_BE_REACHED_NOTICE
-->
${COULD_NOT_BE_REACHED_NOTICE}; a call that was too large to deliver will not succeed on a retry.
