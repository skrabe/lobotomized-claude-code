<!--
name: 'Slash Command: /model — Availability Check Timed Out'
description: >-
  Tells the model the /model availability probe timed out, so the requested
  model was not applied and should be retried.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MODEL_AVAILABILITY_CHECK_TIMED_OUT_VAR_0
  - SLASH_COMMAND_MODEL_AVAILABILITY_CHECK_TIMED_OUT_VAR_1
-->
Couldn't confirm model '${SLASH_COMMAND_MODEL_AVAILABILITY_CHECK_TIMED_OUT_VAR_0(SLASH_COMMAND_MODEL_AVAILABILITY_CHECK_TIMED_OUT_VAR_1)}' is available (the check timed out) · try again
