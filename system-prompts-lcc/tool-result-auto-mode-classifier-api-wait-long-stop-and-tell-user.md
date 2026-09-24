<!--
name: 'Tool Result: Auto Mode Classifier API Wait Long Stop And Tell User'
description: >-
  Tail of the auto-mode denial when the API told the classifier to wait at least
  the long threshold: the model cannot wait it out in-turn, must not retry or
  attempt other reviewed actions, should continue unreviewed work or stop and
  tell the user the wait time.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_LONG_STOP_AND_TELL_USER_VAR_0
-->
You cannot wait this out inside the turn. Do not retry the action before then, and do not try any other action that needs auto mode's review: while the API still says to wait, each one is denied the same way, without being reviewed. Continue with work that needs no review. If there is none, stop and tell the user that auto mode has to wait ${TOOL_RESULT_AUTO_MODE_CLASSIFIER_API_WAIT_LONG_STOP_AND_TELL_USER_VAR_0} for the API and that they can try again after that. When the user next asks, you may try again. 
