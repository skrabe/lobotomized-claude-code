<!--
name: 'Tool Description: ArtifactComments Resume Auto-Replies'
description: >-
  Live-rail paragraph pushed into ArtifactComments' prompt explaining action
  watch with replies:true to resume automatic comment replies.
ccVersion: 2.1.257
-->
**Resuming automatic replies**: `action: "watch"` with `replies: true` and the artifact's `url` re-enables automatic comment replies that were stopped or paused for it (they stop when their live-updates task is killed or the watch is stopped, and pause — the watch kept, until the user's next message — when the user interrupts the session with Ctrl+C / Stop). Use it ONLY when the user has explicitly asked to resume auto-replies; it is approved the way a publish is (a prompt in default mode) and cannot undo the session-wide auto-reply disarm from the kill-all-agents gesture.
