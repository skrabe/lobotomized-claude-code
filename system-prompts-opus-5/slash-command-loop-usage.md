<!--
name: /loop usage text
description: >-
  Usage/help text returned as the /loop command prompt (via getPromptForCommand)
  and injected into the model's turn when no args are given.
ccVersion: 2.1.206
-->
Usage: /loop [interval] <prompt>

Run a prompt or slash command on a recurring interval — or with no interval, let the model self-pace based on the task.

Intervals: Ns, Nm, Nh, Nd (e.g. 5m, 30m, 2h, 1d). Minimum granularity is 1 minute.

Examples:
  /loop 5m /babysit-prs
  /loop 30m check the deploy
  /loop 1h /standup 1
  /loop check the deploy          (dynamic — model picks delays)
  /loop check the deploy every 20m
