<!--
name: 'Data: Bridge worker teardown event'
description: >-
  Schema .describe() for the bridge worker graceful-teardown event — explains it
  is emitted only on opt-in teardown with a reason, that absence is not a
  dead-host signal, and that clients must treat it as a live-tail signal only
ccVersion: 2.1.246
-->
Emitted by the bridge on opt-in graceful worker teardown, only when the teardown caller supplied a reason, before the heartbeat stops, so remote clients can show why the worker went away. Absence is not a dead-host signal: handoffs (/update, /teleport, respawn), auto-disable, mode transitions, and internal fatal-error paths emit nothing; a dead host (battery, OOM, kill -9) never reaches teardown either. This event lands in the durable per-session event stream, so a resumed session may carry historical instances mid-stream — treat it as a live-tail signal (honored only when no further activity follows), not a one-shot session-lifetime fact.
