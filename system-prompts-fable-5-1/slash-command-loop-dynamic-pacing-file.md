<!--
name: /loop dynamic-pacing (loop.md) prompt
description: >-
  Prompt returned by /loop when a loop-tasks file exists and pacing is dynamic,
  sent to the model to run the tasks then self-pace.
ccVersion: 2.1.206
variables:
  - SLASH_COMMAND_LOOP_DYNAMIC_PACING_FILE_VAR_0
  - SLASH_COMMAND_LOOP_DYNAMIC_PACING_FILE_VAR_1
-->
# /loop — loop.md tasks with dynamic pacing

The user invoked \`/loop\` with no prompt and no interval and has a loop-tasks file at \`${SLASH_COMMAND_LOOP_DYNAMIC_PACING_FILE_VAR_0.path}\`. Run those tasks now, then self-pace the next iteration via ${SLASH_COMMAND_LOOP_DYNAMIC_PACING_FILE_VAR_1} — no cron.
