<!--
name: 'Tool Result: Attachment not sent, unsaveable skill'
description: >-
  Tells the model an attachment was not sent because claude.ai would refuse to
  save it as a skill, with the reason and how to fix or rename it
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_ATTACHMENT_NOT_SENT_UNSAVEABLE_SKILL_VAR_0
-->
not sent: claude.ai would refuse to save it as a skill, because ${TOOL_RESULT_ATTACHMENT_NOT_SENT_UNSAVEABLE_SKILL_VAR_0.why}. Fix the file and send it again; to send it only as a download, give the file a name that is not SKILL.md and does not end in .skill
