<!--
name: 'Tool Result: resume_replies denied — session-wide disarm'
description: >-
  Permission-decision message returned by checkPermissions for the Artifact
  tool's resume_replies action; the deny path sends it to the model as the tool
  result. Permission denial saying the kill-all-agents gesture disarmed
  auto-replies for the whole session and a resume cannot reverse it.
ccVersion: 2.1.234
-->
Auto-replies are disarmed for this whole session (the kill-all-agents gesture) and a resume cannot reverse that — a new session re-arms on publish. Nothing here needs approval; do not retry in this session.
