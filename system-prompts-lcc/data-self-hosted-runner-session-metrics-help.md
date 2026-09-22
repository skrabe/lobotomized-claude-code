<!--
name: 'Data: Self-hosted runner session metrics help'
description: >-
  Prometheus HELP text for the runner session lifecycle counters
  (started/completed/failed/interrupted); reaches the model via the read_metrics
  raw payload.
ccVersion: 2.1.261
variables:
  - SELF_HOSTED_RUNNER_METRIC_PREFIX
  - SESSION_LIFECYCLE_METRIC_NAME
-->
# HELP ${SELF_HOSTED_RUNNER_METRIC_PREFIX}_${SESSION_LIFECYCLE_METRIC_NAME} ${SESSION_LIFECYCLE_METRIC_NAME==="sessions_started_total"?"Session child processes spawned over the runner's lifetime. One increment per child spawn; a session that is re-spawned (runner restart, re-assignment) counts again. NOT comparable to the orchestrator's spawn_hooks_total (which counts orchestrator spawn-runner hook runs, including warm hints).":SESSION_LIFECYCLE_METRIC_NAME==="sessions_completed_total"?"Session child processes that ended cleanly over the runner's lifetime: child exited 0, the server closed the session (archive/delete), or the runner released the slot as a clean handoff (idle release, startup timeout, retire / max-session-age release, server deassign). Drain/SIGTERM and the max-lifetime hard-cap kill are NOT counted (those increment sessions_interrupted_total instead).":SESSION_LIFECYCLE_METRIC_NAME==="sessions_failed_total"?"Session child processes that exited with a non-zero code over the runner's lifetime (crash, OOM, spawn error). Does NOT include idle-release or a server deassign the poll loop observed first (those count as completed); a deassign the child notices first via its epoch-409 exit still lands here.":"Session child processes that were terminated for a non-session-outcome reason over its lifetime (drain/SIGTERM, max-lifetime hard-cap kill, released=false backstop, or an external signal). Watchdog and external-signal kills are additionally reported to the server as session failures. Closes the accounting: started - (completed + failed + interrupted) equals the number of session children currently running."}
