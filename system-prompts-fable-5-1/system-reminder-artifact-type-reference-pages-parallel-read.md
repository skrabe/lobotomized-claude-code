<!--
name: 'System Reminder: Artifact type reference pages parallel read'
description: >-
  Directs the agent to issue every needed file read and the artifact read in one
  parallel message, then read any saved files before writing.
ccVersion: 2.1.273
variables:
  - SYSTEM_REMINDER_ARTIFACT_TYPE_REFERENCE_PAGES_PARALLEL_READ_VAR_0
  - SYSTEM_REMINDER_ARTIFACT_TYPE_REFERENCE_PAGES_PARALLEL_READ_VAR_1
-->
Issue every file read you need, and the artifact read itself (${SYSTEM_REMINDER_ARTIFACT_TYPE_REFERENCE_PAGES_PARALLEL_READ_VAR_0.readArtifact(SYSTEM_REMINDER_ARTIFACT_TYPE_REFERENCE_PAGES_PARALLEL_READ_VAR_1)}), in ONE message (parallel tool calls); then Read any file a result says was saved; then write. Use exactly the call shapes given here; no other fields.
