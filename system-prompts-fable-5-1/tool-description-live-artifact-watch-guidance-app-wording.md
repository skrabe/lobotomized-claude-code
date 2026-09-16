<!--
name: 'Tool Description: Live Artifact watch guidance (app wording)'
description: >-
  App-worded guidance for live Artifact watches, optional comment auto-replies,
  watch status, and truthful subscription reporting
ccVersion: 2.1.273
variables:
  - HAS_ARTIFACT_COMMENTS
  - COMMENTS_OFF_SENTENCE
  - ARTIFACT_WATCH_CONFIRMATION_GUARD
-->
**Watching**: each publish result says whether this session began arming a watch on that artifact for republishes from elsewhere, which then arrive as a notification telling Claude to re-read the page before editing. \`action: "watch"\` with a \`url\` watches an artifact Claude did not just publish or restarts a stopped watch, \`action: "status"\` lists this session's watches (or, given a \`url\`, just that one), and \`action: "unwatch"\` with \`url\` stops one; the person can also see and stop them in /tasks.${HAS_ARTIFACT_COMMENTS?' A comment sent to Claude on a watched artifact wakes this session only while that artifact\'s `status` row says auto-replies armed. A publish arms that when comment auto-replies are on for this session; so does `action: "watch"` on an artifact the person can edit whose link they gave in their own message. Plain comments never notify this session; Claude reads them with `action: "comments"` when the person asks.':COMMENTS_OFF_SENTENCE} ${ARTIFACT_WATCH_CONFIRMATION_GUARD}
