<!--
name: 'Data: Self-hosted orchestrator session queue wait by reason metric help'
description: >-
  Prometheus HELP text for the orchestrator's queue-wait histogram split by
  spawn reason
ccVersion: 2.1.328
-->
# HELP claude_code_self_hosted_orchestrator_session_queue_wait_by_reason_seconds Seconds a session waited in the queue before the orchestrator claimed it: the observations of claude_code_self_hosted_orchestrator_session_queue_wait_seconds, by the reason Anthropic gave for the spawn hint (CLAUDE_RUNNER_SPAWN_REASON). reason="session_created": a new session, first try; reason="resumed": a released or paused session that was re-opened, first try. A retry counts under its own reason. reason="none": no reason given; reason="other": a reason this version does not know.
