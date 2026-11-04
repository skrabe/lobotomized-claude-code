<!--
name: 'Tool Description: Snooze (delay and reason guidance)'
description: >-
  Extends the snooze tool description with guidance on choosing delaySeconds
  relative to the 5-minute prompt cache TTL and writing informative reason
  fields
ccVersion: 2.1.284
variables:
  - TOOL_DESCRIPTION_SNOOZE_DELAY_AND_REASON_GUIDANCE_VAR_0
  - TOOL_DESCRIPTION_SNOOZE_DELAY_AND_REASON_GUIDANCE_VAR_1
  - TOOL_DESCRIPTION_SNOOZE_DELAY_AND_REASON_GUIDANCE_VAR_2
-->

Resume work in /loop dynamic mode: the user invoked /loop without an interval.

For harness-tracked background work, rely on completion notifications and use a fallback of at least 1200s. For external work the harness cannot track, match the delay to how fast its state changes.

Pass the same /loop prompt verbatim each turn. For autonomous loops with no user prompt, pass \`${TOOL_DESCRIPTION_SNOOZE_DELAY_AND_REASON_GUIDANCE_VAR_0}\`; the runtime resolves it when the wakeup fires. End the loop with \`stop: true\` alone.
