<!--
name: 'Data: Runner session_idle_seconds metric help'
description: >-
  Prometheus HELP line for the per-session idle gauge; reaches the model via the
  read_metrics raw payload.
ccVersion: 2.1.224
variables:
  - DATA_SELF_HOSTED_RUNNER_SESSION_IDLE_METRIC_HELP_VAR_0
-->
# HELP ${DATA_SELF_HOSTED_RUNNER_SESSION_IDLE_METRIC_HELP_VAR_0}_session_idle_seconds Seconds since the session went idle (turn-end or awaiting-action); 0 while a turn is running, background work is pending, or the session is initializing. One series per active session; disappears at session end.

