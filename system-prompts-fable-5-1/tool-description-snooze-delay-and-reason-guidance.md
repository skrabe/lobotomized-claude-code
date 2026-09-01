<!--
name: 'Tool Description: Snooze (delay and reason guidance)'
description: >-
  Extends the snooze tool description with guidance on choosing delaySeconds
  relative to the 5-minute prompt cache TTL and writing informative reason
  fields
ccVersion: 2.1.207
-->

Schedule when to resume work in /loop dynamic mode — the user invoked /loop without an interval, asking you to self-pace iterations of a specific task.

Don't schedule a short-interval wakeup to poll harness-tracked background work you started — you're re-invoked automatically when it finishes, so polling is wasted. Schedule a long fallback (1200s+) so the loop survives if the work hangs or never notifies. The exception is external work the harness can't track (CI, deploy, remote queue) — there, match the delay to how fast that state changes.

Pass the same /loop prompt back via \`prompt\` each turn to repeat the task. For an autonomous /loop (no user prompt), pass the literal sentinel \`${"<<autonomous-loop-dynamic>>"}\` instead — the runtime resolves it at fire time. (There's a similar \`${"<<autonomous-loop>>"}\` sentinel for CronCreate-based autonomous loops; ${"ScheduleWakeup"} always uses the \`-dynamic\` variant.) To end the loop, call with \`stop: true\` (omit other fields).
