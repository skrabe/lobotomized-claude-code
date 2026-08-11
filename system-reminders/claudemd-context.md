<!--
name: claudeMd context wrapper
description: >-
  Per-turn <system-reminder> that bundles { claudeMd, userEmail, currentDate }
  into a 'As you answer the user's questions...' block. Empty .md body =
  suppress entirely.
ccVersion: 2.1.141
placeholders:
  - context_blocks
shadows:
  - system-reminder-question-context
-->
As you answer the user's questions, you can use the following context:
{{context_blocks}}

      This context may or may not be relevant; draw on it only where it bears on the task.
