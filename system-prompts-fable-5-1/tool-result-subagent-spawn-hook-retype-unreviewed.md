<!--
name: Subagent Spawn Hook Retype Unreviewed
description: >-
  Agent-tool error when a plugin agent.spawn hook retargets a web-fetch spawn
  that skipped classifier review.
ccVersion: 2.1.261
-->
A plugin's agent.spawn hook named another agent for a web-fetch dispatch admitted without classifier review; it cannot run unconfined. Dispatch that agent directly.
