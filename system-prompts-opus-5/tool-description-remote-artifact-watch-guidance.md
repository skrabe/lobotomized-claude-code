<!--
name: 'Tool Description: Remote artifact watch guidance'
description: >-
  Explains durable remote artifact wake subscriptions, registration, comment
  wakes, and truthful watch-status reporting
ccVersion: 2.1.273
variables:
  - HAS_ARTIFACT_COMMENTS
  - ARTIFACT_WATCH_STATUS_GUIDANCE
  - REMOTE_ARTIFACT_WATCH_NOTE
-->
so on a wake Claude re-reads the artifact${HAS_ARTIFACT_COMMENTS?" (and its comments, on a comment wake)":""} before editing. Each publish result says whether that artifact's watch began registering; \`action: "watch"\` with a \`url\` watches an artifact Claude did not just publish, \`action: "status"\` lists the watches that registered and what wakes each (or, given a \`url\`, just that one), and \`action: "unwatch"\` with \`url\` stops one.${HAS_ARTIFACT_COMMENTS?' Plain comments never wake this session; Claude reads them with `action: "comments"` when the person asks.':ARTIFACT_WATCH_STATUS_GUIDANCE} ${REMOTE_ARTIFACT_WATCH_NOTE}
