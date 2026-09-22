<!--
name: 'Tool Result: Artifact Durable Wake Subscribe Forbidden'
description: >-
  Durable-wake failure reason when the artifact service refuses wake
  subscriptions from this session until it ends.
ccVersion: 2.1.246
-->
The artifact service refuses wake subscriptions from this session, for any artifact until the session ends, so retrying will not help. Later publishes in this session are not armed; only an explicit watch re-checks with the service.
