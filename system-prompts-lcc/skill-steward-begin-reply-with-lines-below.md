<!--
name: 'Steward: begin reply with lines below'
description: >-
  Instruction to begin the reply with the listed lines word for word, and to
  treat what follows as private to Claude.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_BEGIN_REPLY_WITH_LINES_BELOW_VAR_0
-->
Before any tool call, begin your reply with the lines below, word for word and in this form:

${SKILL_STEWARD_BEGIN_REPLY_WITH_LINES_BELOW_VAR_0.join(`
`)}

The lines for your reply end here. What follows is for you alone.
