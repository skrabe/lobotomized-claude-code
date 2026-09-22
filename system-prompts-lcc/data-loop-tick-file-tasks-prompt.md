<!--
name: /loop tick dynamic-tasks prompt
description: >-
  The /loop tick prompt built from the loop-tasks file, instructing the model to
  work through the configured tasks each tick; injected as a turn message into
  model context.
ccVersion: 2.1.206
variables:
  - DATA_LOOP_TICK_FILE_TASKS_PROMPT_VAR_0
  - DATA_LOOP_TICK_FILE_TASKS_PROMPT_VAR_1
-->
# /loop tick — tasks from ${DATA_LOOP_TICK_FILE_TASKS_PROMPT_VAR_0.path}

The user configured a loop-tasks file. Work through the tasks defined below; these are the instructions for this tick and every subsequent tick (the reminder on later fires refers back to this message).

---

${DATA_LOOP_TICK_FILE_TASKS_PROMPT_VAR_0.content}

---

${DATA_LOOP_TICK_FILE_TASKS_PROMPT_VAR_1}
