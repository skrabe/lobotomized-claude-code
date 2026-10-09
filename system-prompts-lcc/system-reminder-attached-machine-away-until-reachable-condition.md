<!--
name: 'System Reminder: Attached machine away until-reachable condition'
description: >-
  Defers further calls to an attached machine until a later attached-machines
  note reports it reachable again or the user says it is back or asks to try
  again
ccVersion: 2.1.295
variables:
  - REMOTE_MACHINE_NAME
-->
until a later attached-machines note says ${REMOTE_MACHINE_NAME} is reachable again, or the user says it is back or asks you to try again
