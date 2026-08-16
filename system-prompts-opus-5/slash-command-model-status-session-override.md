<!--
name: 'Slash Command: /model — session model overridden by plan mode'
description: >-
  Tells the model that a plan-mode session override is in force and separates
  the model actually running from the configured base model, so it does not
  misreport which model is active.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MODEL_STATUS_SESSION_OVERRIDE_VAR_0
  - SLASH_COMMAND_MODEL_STATUS_SESSION_OVERRIDE_VAR_1
  - SLASH_COMMAND_MODEL_STATUS_SESSION_OVERRIDE_VAR_2
  - SLASH_COMMAND_MODEL_STATUS_SESSION_OVERRIDE_VAR_3
  - SLASH_COMMAND_MODEL_STATUS_SESSION_OVERRIDE_VAR_4
-->
Current model: ${SLASH_COMMAND_MODEL_STATUS_SESSION_OVERRIDE_VAR_0(SLASH_COMMAND_MODEL_STATUS_SESSION_OVERRIDE_VAR_1(SLASH_COMMAND_MODEL_STATUS_SESSION_OVERRIDE_VAR_2.mainLoopModelForSession))} (session override from plan mode)
Base model: ${SLASH_COMMAND_MODEL_STATUS_SESSION_OVERRIDE_VAR_3}${SLASH_COMMAND_MODEL_STATUS_SESSION_OVERRIDE_VAR_4}
