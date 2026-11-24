<!--
name: 'Steward: begin reply verbatim lead'
description: >-
  Instruction to start the reply, before any tool call, with the given lines or
  paragraph word for word as plain text.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_BEGIN_REPLY_VERBATIM_LEAD_VAR_0
-->
Before any tool call, begin your reply with ${SKILL_STEWARD_BEGIN_REPLY_VERBATIM_LEAD_VAR_0==="lines"?"these":"this"} ${SKILL_STEWARD_BEGIN_REPLY_VERBATIM_LEAD_VAR_0}, word for word, as plain text, without the ">":
