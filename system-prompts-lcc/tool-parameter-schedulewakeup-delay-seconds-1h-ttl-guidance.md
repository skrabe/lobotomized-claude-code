<!--
name: 'Tool Parameter: ScheduleWakeup delaySeconds (1-hour TTL guidance)'
description: >-
  ScheduleWakeup tool's 'Picking delaySeconds' guidance shown when the session's
  prompt-cache TTL is 1 hour
ccVersion: 2.1.284
-->

## Picking delaySeconds

This route uses a 1-hour prompt-cache TTL; the runtime clamps delays to [60, 3600] seconds. Pace checks by state changes, rather than scheduling wakeups to keep the cache warm. Use at least 1200s for fallback heartbeats, or 1200s–1800s for idle ticks with no specific signal to watch.
