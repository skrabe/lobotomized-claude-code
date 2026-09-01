<!--
name: /loop schedule summary directive
description: >-
  Fragment of the /loop schedule prompt telling the model what to report about
  the scheduled cron, injected into model context.
ccVersion: 2.1.206
variables:
  - SLASH_COMMAND_LOOP_SCHEDULE_SUMMARY_DIRECTIVE_VAR_0
  - SLASH_COMMAND_LOOP_SCHEDULE_SUMMARY_DIRECTIVE_VAR_1
  - SLASH_COMMAND_LOOP_SCHEDULE_SUMMARY_DIRECTIVE_VAR_2
-->
what's scheduled, the cron expression, the human-readable cadence, that it's running tasks from \`${SLASH_COMMAND_LOOP_SCHEDULE_SUMMARY_DIRECTIVE_VAR_0.path}\`, that recurring tasks auto-expire after ${SLASH_COMMAND_LOOP_SCHEDULE_SUMMARY_DIRECTIVE_VAR_1} days, and that the user can cancel sooner with ${SLASH_COMMAND_LOOP_SCHEDULE_SUMMARY_DIRECTIVE_VAR_2} (include the job ID).
