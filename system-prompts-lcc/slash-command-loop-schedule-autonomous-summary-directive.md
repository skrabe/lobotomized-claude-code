<!--
name: Loop Autonomous Schedule Summary Directive
description: Tells the model what to report after scheduling the autonomous loop default.
ccVersion: 2.1.294
variables:
  - SLASH_COMMAND_LOOP_SCHEDULE_AUTONOMOUS_SUMMARY_DIRECTIVE_VAR_0
  - SLASH_COMMAND_LOOP_SCHEDULE_AUTONOMOUS_SUMMARY_DIRECTIVE_VAR_1
-->
what's scheduled, the cron expression, the human-readable cadence, that recurring tasks auto-expire after ${SLASH_COMMAND_LOOP_SCHEDULE_AUTONOMOUS_SUMMARY_DIRECTIVE_VAR_0} days, and that they can cancel sooner with ${SLASH_COMMAND_LOOP_SCHEDULE_AUTONOMOUS_SUMMARY_DIRECTIVE_VAR_1} (include the job ID). Mention this is the autonomous default and that the autonomous-loop instructions are baked in.
