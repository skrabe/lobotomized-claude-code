<!--
name: 'System Reminder: Approved Claude Doc plan inline edits'
description: >-
  Tells the model the approved Doc text included here overrides its draft, that
  missing steps were removed on purpose, and to summarize the user's changes
  before starting
ccVersion: 2.1.319
variables:
  - SYSTEM_REMINDER_APPROVED_CLAUDE_DOC_PLAN_INLINE_EDITS_VAR_0
  - SYSTEM_REMINDER_APPROVED_CLAUDE_DOC_PLAN_INLINE_EDITS_VAR_1
-->
${SYSTEM_REMINDER_APPROVED_CLAUDE_DOC_PLAN_INLINE_EDITS_VAR_0} Where it differs from what you last wrote, the user changed it: a step that is missing was removed on purpose, and carrying it out because you remember writing it would undo their edit. Work to the Doc as it reads here: it is the user's instruction, and following your draft would drop their corrections while they believe that the work follows their plan. If you have not started the work yet, say in one line what they changed, or that nothing changed, then start.

${SYSTEM_REMINDER_APPROVED_CLAUDE_DOC_PLAN_INLINE_EDITS_VAR_1}
