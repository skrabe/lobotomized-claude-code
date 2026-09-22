<!--
name: 'System Reminder: Safety Classifier Interrupted Tool Exception'
description: >-
  Exception clause on the safety-classifier stop nudge covering a tool that may
  have already completed.
ccVersion: 2.1.273
-->
 Exception: a tool call whose result reads "Interrupted" was already running when the response was stopped; it may have partially or fully completed.
