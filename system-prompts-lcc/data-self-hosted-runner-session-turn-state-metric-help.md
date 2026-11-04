<!--
name: 'Data: Runner session_turn_state metric help'
description: >-
  Prometheus HELP line for the per-session turn state gauge explaining the busy,
  waiting, rest and lost states; reaches the model via the read_metrics raw
  payload
ccVersion: 2.1.318
variables:
  - DATA_SELF_HOSTED_RUNNER_SESSION_TURN_STATE_METRIC_HELP_VAR_0
-->
# HELP ${DATA_SELF_HOSTED_RUNNER_SESSION_TURN_STATE_METRIC_HELP_VAR_0}_session_turn_state The turn state the server reports for a session whose tools this runner hosts, in the state label; the value is always 1. busy: a worker holds the session. waiting: a question is waiting for the user. rest: no worker, and the last one reported idle. lost: no worker, and the last one did not report idle, or none has started.
