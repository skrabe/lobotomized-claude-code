<!--
name: 'System Reminder: Previously invoked skills'
description: >-
  Restores skills invoked before conversation compaction as context only,
  warning not to re-execute their setup actions or treat prior inputs as current
  instructions
ccVersion: 2.1.119
variables:
  - FORMATTED_SKILLS_LIST
-->
These skills were invoked earlier in this session, before compaction. Shown for context only — don't re-execute their setup actions (scheduling, file creation). The "## Input" sections show the original arguments from when each skill first ran; they aren't the current user message. Apply ongoing behavioral guidelines where still relevant.

${FORMATTED_SKILLS_LIST}
