<!--
name: 'Tool Description: ScheduleWakeup delay and reason guidance'
description: >-
  Composite ScheduleWakeup tool-description extension covering noop reporting,
  cache-aware delaySeconds selection, and the reason field.
ccVersion: 2.1.246
variables:
  - SCHEDULE_WAKEUP_BASE_DESCRIPTION
  - PROMPT_CACHE_TTL_CLASSIFICATION
-->
${SCHEDULE_WAKEUP_BASE_DESCRIPTION}

${'Consecutive `noop: true` ticks are collapsed in the user\'s terminal view and tracked as a streak, so long quiet holds stay legible to the user without scrolling.'}

## Picking delaySeconds

Match the delay to what you are actually waiting for. Polling external state the harness cannot notify you about (a CI run, a deploy, a remote queue): pick the delay from how fast that state changes — a ~8-minute CI run gets one ~480s check, not eight 60s ones. A fallback heartbeat behind another wake signal (a Monitor, a task notification): 1200s+. Idle ticks with nothing specific to watch: 1200s–1800s. Never schedule extra wakeups to keep the prompt cache warm. The runtime clamps to [60, 3600].

${`## The reason field

One short sentence on what you chose and why. Goes to telemetry and is shown back to the user. "watching CI run" beats "waiting." The user reads this to understand what you're doing without having to predict your cadence in advance — make it specific.`}
