<!--
name: /loop dynamic-pacing (autonomous) prompt
description: >-
  Prompt returned by /loop with no prompt/interval in dynamic pacing mode, sent
  to the model to run the autonomous check then self-pace.
ccVersion: 2.1.206
variables:
  - SLASH_COMMAND_LOOP_DYNAMIC_PACING_AUTONOMOUS_VAR_0
-->
# /loop — autonomous default with dynamic pacing

The user invoked \`/loop\` with no prompt and no interval. Run the autonomous check now, then self-pace the next iteration via ${SLASH_COMMAND_LOOP_DYNAMIC_PACING_AUTONOMOUS_VAR_0} — no cron.
