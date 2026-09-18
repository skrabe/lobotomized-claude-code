<!--
name: 'System Reminder: Artifact Opening Bash And Read Parallel'
description: >-
  When a url read is already asked, instruct a parallel Bash call plus the
  artifact read, then write.
ccVersion: 2.1.273
variables:
  - SYSTEM_REMINDER_ARTIFACT_OPENING_BASH_AND_READ_PARALLEL_VAR_0
  - SYSTEM_REMINDER_ARTIFACT_OPENING_BASH_AND_READ_PARALLEL_VAR_1
-->
Make that Bash call and the artifact read itself, ${SYSTEM_REMINDER_ARTIFACT_OPENING_BASH_AND_READ_PARALLEL_VAR_0.readArtifact(SYSTEM_REMINDER_ARTIFACT_OPENING_BASH_AND_READ_PARALLEL_VAR_1)}, in ONE message (parallel tool calls); then write.
