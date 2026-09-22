<!--
name: Artifact watch re-latch permission ask
description: >-
  Disclosure appended to the ask when re-watching an artifact whose watch was
  deliberately stopped earlier in this session.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_RELATCH_PERMISSION_ASK_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCH_RELATCH_PERMISSION_ASK_VAR_1
-->
approving resumes republish notifications${TOOL_RESULT_ARTIFACT_WATCH_RELATCH_PERMISSION_ASK_VAR_0?" (and, in a cloud session, the wake when a comment on it is sent to Claude, which Claude may then read and answer)":""} for the rest of this session${TOOL_RESULT_ARTIFACT_WATCH_RELATCH_PERMISSION_ASK_VAR_1?" and, if you can edit it and gave its link, lets comments sent to Claude reach this session again, where Claude may answer them unattended — unless its auto-replies were stopped (those stay stopped until you ask to resume them; auto-replies only paused by an interrupt — Ctrl+C or Stop — do resume)":""}; republish notifications carry no content
