<!--
name: 'Agent Prompt: Narration next-line rule'
description: >-
  Narration prompt rule restricting the next: line to a step the conversation
  already states, otherwise replying with the now: line alone
ccVersion: 2.1.234
-->
The next line restates, it never predicts: include it only when the conversation above — thinking, prose, or a task list — already names the step that follows, and that step is still ahead. If no upcoming step is stated, or now: is the last one — usually the case near the end of a task — reply with the now: line alone.
