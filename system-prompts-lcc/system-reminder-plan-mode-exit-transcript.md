<!--
name: Post-plan-mode transcript pointer
description: >-
  Instruction appended to the model's context on exiting plan mode telling it
  where to read the full transcript for earlier details.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_PLAN_MODE_EXIT_TRANSCRIPT_VAR_0
-->


If you need specific details from before exiting plan mode (like exact code snippets, error messages, or content you generated), read the full transcript at: ${SYSTEM_REMINDER_PLAN_MODE_EXIT_TRANSCRIPT_VAR_0()}
