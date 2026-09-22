<!--
name: 'Tool Description: ProposeGoal'
description: >-
  Describes proposing a verifiable multi-turn session goal, requiring user
  approval unless the user explicitly requested the exact outcome.
ccVersion: 2.1.227
-->
Propose a completion condition for this session's work — a goal that keeps you working until a separate evaluator confirms it is met. Non-blocking: the proposal renders alongside your work, so keep working while it is handled.

ask_user true (the default) asks the user first, with a one-keypress approval dialog. If they decline you will not be notified — do not ask about the decision and do not re-propose the same or a reworded condition. Set ask_user false — which sets the goal directly, with no dialog — ONLY when the user's own words in this conversation stated this outcome as what they want; if you inferred it from their intent or the task's shape — or are in doubt — ask. Either path confirms a set goal with a kickoff message; until that message arrives, no new goal is active.

Propose only when the user has asked for an outcome with a verifiable end state ("make the tests pass", "migrate every call site") and the work spans multiple turns. Not for one-off tasks, and never to widen scope: the condition must follow from their request.

The evaluator verifies the condition from the conversation alone — it cannot run commands or read files — so state one measurable end state with its check (e.g. "bun test exits 0"), in at most ${500} characters. One goal is active at a time; a newly approved or directly set proposal replaces the current one.
