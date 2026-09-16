<!--
name: 'System Reminder: Artifact Opening Bash And Read If Edited'
description: >-
  When a url read is not forced, instruct a parallel Bash call and an artifact
  read only if the user may have edited it.
ccVersion: 2.1.273
variables:
  - SYSTEM_REMINDER_ARTIFACT_OPENING_BASH_AND_READ_IF_EDITED_VAR_0
  - SYSTEM_REMINDER_ARTIFACT_OPENING_BASH_AND_READ_IF_EDITED_VAR_1
-->
Make that Bash call (and the artifact read itself, ${SYSTEM_REMINDER_ARTIFACT_OPENING_BASH_AND_READ_IF_EDITED_VAR_0.readArtifact(SYSTEM_REMINDER_ARTIFACT_OPENING_BASH_AND_READ_IF_EDITED_VAR_1)}, only if the user may have edited it) in ONE message (parallel tool calls); then write.
