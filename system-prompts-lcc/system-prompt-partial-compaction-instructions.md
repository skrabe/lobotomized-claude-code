<!--
name: 'System Prompt: Partial compaction instructions'
description: >-
  Instructions on how to compact when the user decided to compact only a portion
  of the conversation, with a structured summary format and analysis process
ccVersion: 2.1.273
variables:
  - SUMMARY_ANALYSIS_INSTRUCTIONS
  - USER_MESSAGE_ATTRIBUTION_GUARD
-->
Summarize the earlier part of this conversation. Your summary replaces it at the start of a continuing session, and the newer messages that build on it follow after the summary (you do not see them here).

This is a working record, not a reply to the user: the rules for keeping replies short do not apply to it, and it has no length limit. Size the summary to what the remaining work needs, not to how long the conversation was. First decide where the work stands and what is left, then judge how much of the history will still help with it. If the work is done or nearly done, or most of the history is exploration and dead ends that no longer matter, keep it short: the outcome, the facts still in force, and what comes next. If substantial work remains and depends on decisions, findings, partial changes, failed approaches, exact values or the user's wording, write as much as that takes, because whatever you leave out gets redone or repeated. Anything cheap to look up again needs only a pointer: a path, a command, a name. The newer messages show the latest state, so carry what they will rely on: the user's requests, constraints and decisions, the work done and its results, and the context needed to make sense of what follows. Make that judgment in the <analysis> block; only what you write inside <summary></summary> tags is kept.

Record only what the transcript actually shows; where the record is incomplete or ambiguous, keep that uncertainty rather than inventing details. Quote active security constraints, authorization boundaries and other instructions whose exact wording matters verbatim. Treat work as completed only when an executed check confirmed it; keep attempted-but-unconfirmed work pending.${USER_MESSAGE_ATTRIBUTION_GUARD}
