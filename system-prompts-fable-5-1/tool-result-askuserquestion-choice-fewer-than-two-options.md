<!--
name: 'Tool Result: AskUserQuestion Choice Fewer Than Two Options'
description: >-
  validationErrorSteer appended to the AskUserQuestion tool error when a choice
  question has fewer than two options, so the person never saw it.
ccVersion: 2.1.261
-->
This call included a choice question with fewer than 2 options, so it was rejected and the person never saw it. If that question is open-ended, re-ask it with "kind": "text" and no options; if there is really only one path, state it as the approach you are taking and continue with the task. Do not invent a filler second option.
