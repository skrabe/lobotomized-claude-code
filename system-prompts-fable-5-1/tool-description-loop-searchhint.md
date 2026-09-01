<!--
name: Loop tool self-pace hint
description: >-
  searchHint/prompt for the dynamic /loop tool surfaced to the model describing
  how to self-pace or stop the loop.
ccVersion: 2.1.206
variables:
  - TOOL_DESCRIPTION_LOOP_SEARCHHINT_VAR_0
-->
self-pace the dynamic /loop: pick a delay before the next tick, or stop/end/cancel the dynamic loop with stop:true (a fixed-interval /loop is a recurring cron — cancel it with ${TOOL_DESCRIPTION_LOOP_SEARCHHINT_VAR_0})
