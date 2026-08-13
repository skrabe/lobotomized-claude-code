<!--
name: 'Tool parameter: Artifact action — watch/unwatch/status'
description: >-
  Addendum to the Artifact tool's action parameter describing the watch,
  unwatch, and status actions.
ccVersion: 2.1.231
-->
 'watch' opens a live-update subscription to the artifact at `url` so this session is notified when another session republishes it; 'unwatch' stops that subscription; 'status' lists this session's artifact watches (pass `url` to check one). Watches live only as long as this session. In a remote session there is no live stream: 'watch' registers a durable wake subscription instead, so this session is woken with a new turn when the artifact is next published or a comment on it is sent to Claude (no live updates; on wake re-read the artifact — and its comments, on a comment wake).
