<!--
name: 'Memory: repo-state snapshots are frozen'
description: >-
  Guidance in the Memory system prompt that repo-state memories are frozen in
  time; prefer git log.
ccVersion: 2.1.206
-->
A memory that summarizes repo state (activity logs, architecture snapshots) is frozen in time. If the user asks about *recent* or *current* state, prefer `git log` or reading the code over recalling the snapshot.
