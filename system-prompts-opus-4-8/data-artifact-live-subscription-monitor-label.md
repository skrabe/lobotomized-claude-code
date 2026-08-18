<!--
name: 'Data: Artifact watch monitor description'
description: >-
  Background-monitor description for an artifact live subscription; echoed to
  the model as the Monitor event title in the injected task-notification.
ccVersion: 2.1.234
variables:
  - DATA_ARTIFACT_LIVE_SUBSCRIPTION_MONITOR_LABEL_VAR_0
  - DATA_ARTIFACT_LIVE_SUBSCRIPTION_MONITOR_LABEL_VAR_1
  - DATA_ARTIFACT_LIVE_SUBSCRIPTION_MONITOR_LABEL_VAR_2
-->
live updates for artifact ${DATA_ARTIFACT_LIVE_SUBSCRIPTION_MONITOR_LABEL_VAR_0} (${DATA_ARTIFACT_LIVE_SUBSCRIPTION_MONITOR_LABEL_VAR_1?"watch requested":DATA_ARTIFACT_LIVE_SUBSCRIPTION_MONITOR_LABEL_VAR_2.armedVia==="attach"?"attached via /artifacts":DATA_ARTIFACT_LIVE_SUBSCRIPTION_MONITOR_LABEL_VAR_2.armedVia==="resume"?"resume requested":"auto-armed on publish"})
