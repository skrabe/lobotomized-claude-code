<!--
name: /loop schedule loop.md prompt
description: >-
  Prompt returned by /loop to schedule a recurring cron for loop.md tasks then
  run the first tick, sent to the model.
ccVersion: 2.1.206
variables:
  - SLASH_COMMAND_LOOP_SCHEDULE_FILE_VAR_0
  - SLASH_COMMAND_LOOP_SCHEDULE_FILE_VAR_1
-->
# /loop — schedule loop.md tasks

The user invoked \`/loop\` with no prompt (input was empty or just the interval \`${SLASH_COMMAND_LOOP_SCHEDULE_FILE_VAR_0}\`) and has a loop-tasks file at \`${SLASH_COMMAND_LOOP_SCHEDULE_FILE_VAR_1.path}\`. Schedule a recurring cron that runs those tasks each tick, then run the first tick immediately.
