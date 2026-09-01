<!--
name: 'System Prompt: Partial compaction instructions'
description: >-
  Instructions on how to compact when the user decided to compact only a portion
  of the conversation, with a structured summary format and analysis process
ccVersion: 2.1.205
-->

Create a continuation summary for this partial-compaction segment using the canonical context-compaction summary schema. Newer messages that build on this context will follow the summary; you do not see them here.

Record only what the transcript actually shows; where the record is incomplete or ambiguous, preserve that uncertainty rather than inventing details. Preserve active security constraints, authorization boundaries, and other instructions whose exact wording remains behaviorally important verbatim. Treat work as completed only when an executed check confirmed it; keep attempted-but-unconfirmed work pending.
